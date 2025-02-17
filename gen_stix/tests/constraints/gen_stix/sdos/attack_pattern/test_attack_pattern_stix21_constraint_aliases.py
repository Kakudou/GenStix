import os
import json

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers


from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder import (
    CreateAttackPatternInputPortBuilder,
)

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_constraint_aliases.constraint",
    "Creating an AttackPattern with invalid aliases.",
)
def test_attack_pattern_stix21_constraint_aliases():
    pass


@given(
    parsers.parse(
        "An AttackPattern is created with a {type_}, {name}, and invalid {aliases}."
    ),
    target_fixture="context",
)
def given_attack_pattern_stix21_constraint_aliases(type_, name, aliases):
    input_contract = (
        CreateAttackPatternInputPortBuilder()
        .create()
        .with_type_(type_)
        .with_name(name)
    )

    return {"aliases": aliases, "input_contract": input_contract}


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_constraint_aliases(context):
    aliases = {}
    try:
        aliases = json.loads(context["aliases"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_aliases(aliases)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A TypeError should be raised, stating that {aliases} should be a list of strings."
    )
)
def then_attack_pattern_stix21_constraint_aliases(context, aliases):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`aliases` must be a List[str]."
