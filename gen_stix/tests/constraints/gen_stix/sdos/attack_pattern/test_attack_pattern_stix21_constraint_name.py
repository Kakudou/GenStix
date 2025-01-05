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
    "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_constraint_name.constraint",
    "Creating an AttackPattern with an invalid name.",
)
def test_attack_pattern_stix21_constraint_name():
    pass


@given(
    parsers.parse(
        "An AttackPattern is created with a {name} that is not a string and a valid {type_}."
    ),
    target_fixture="context",
)
def given_attack_pattern_stix21_constraint_name(name, type_):
    input_contract = (
        CreateAttackPatternInputPortBuilder().create().with_type_(type_)
    )

    return {"name": json.loads(name), "input_contract": input_contract}


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_constraint_name(context):
    try:
        context["input_contract"].with_name(context["name"])
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A TypeError should be raised, stating that the value of name must be a string."
    )
)
def then_attack_pattern_stix21_constraint_name(context):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`name` must be a str."
