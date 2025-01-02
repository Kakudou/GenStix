import os
import json

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.src.gen_stix.usecase.\
     sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder\
     import CreateAttackPatternInputPortBuilder

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_constraint_external_references.constraint",
          "Creating an AttackPattern with invalid external_references.")
def test_attack_pattern_stix21_constraint_external_references():
    pass


@given(parsers.parse("An AttackPattern is created with a {type_}, {name}, and invalid {external_references}."), target_fixture="context")
def given_attack_pattern_stix21_constraint_external_references(type_, name, external_references):
    input_contract = CreateAttackPatternInputPortBuilder()\
        .create()\
        .with_type_(type_)\
        .with_name(name)

    return {
        "external_references": external_references,
        "input_contract": input_contract
    }


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_constraint_external_references(context):
    external_references = {}
    external_references = json.loads(context["external_references"])
    try:
        context["input_contract"].with_external_references(external_references)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(parsers.parse("A ValueError should be raised, stating that {external_references} should be a list of external-references."))
def then_attack_pattern_stix21_constraint_external_references(context, external_references):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`external_references` must be a List[external-reference]."
