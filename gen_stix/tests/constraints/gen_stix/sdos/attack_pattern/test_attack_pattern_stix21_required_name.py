import os

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
          "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_required_name.constraint",
          "Creating an AttackPattern without a name.")
def test_attack_pattern_stix21_required_name():
    pass


@given(parsers.parse("An AttackPattern is created without any name but with a {type_}."), target_fixture="context")
def given_attack_pattern_stix21_required_name(type_):
    input_contract = CreateAttackPatternInputPortBuilder()\
        .create()\
        .with_type_(type_)

    return {
        "input_contract": input_contract
    }


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_required_name(context):
    try:
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(parsers.parse("A ValueError should be raised, stating the requirements for the name field."))
def then_attack_pattern_stix21_required_name(context):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`name` is a required field for AttackPattern"
