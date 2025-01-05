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
    "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_constraint_type.constraint",
    "Creating an AttackPattern with an invalid type.",
)
def test_attack_pattern_stix21_constraint_type():
    pass


@given(
    parsers.parse(
        "An AttackPattern is created with a {type_} different from `attack-pattern` and a valid {name}."
    ),
    target_fixture="context",
)
def given_attack_pattern_stix21_constraint_type(type_, name):
    input_contract = (
        CreateAttackPatternInputPortBuilder().create().with_name(name)
    )

    return {"type_": type_, "input_contract": input_contract}


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_constraint_type(context):
    type_ = {}
    try:
        type_ = json.loads(context["type_"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_type_(type_)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A ValueError should be raised, stating that the value of type must be `attack-pattern`."
    )
)
def then_attack_pattern_stix21_constraint_type(context):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`type` must be `attack-pattern`."
