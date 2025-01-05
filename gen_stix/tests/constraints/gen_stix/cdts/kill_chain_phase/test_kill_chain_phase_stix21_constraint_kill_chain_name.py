import os
import json

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers


from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_inputport_builder import (
    CreateKillChainPhaseInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/constraints/gen_stix/cdts/kill_chain_phase/kill_chain_phase_stix21_constraint_kill_chain_name.constraint",
    "Creating an object with an invalid kill_chain_name format.",
)
def test_kill_chain_phase_stix21_constraint_kill_chain_name():
    pass


@given(
    parsers.parse(
        "An object is created with a {kill_chain_name} that is not all lowercase or contains spaces/underscores and a valid {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_stix21_constraint_kill_chain_name(
    kill_chain_name, phase_name
):
    input_contract = (
        CreateKillChainPhaseInputPortBuilder()
        .create()
        .with_kill_chain_name(kill_chain_name)
        .with_phase_name(phase_name)
    )

    return {
        "kill_chain_name": kill_chain_name,
        "input_contract": input_contract,
    }


@when(parsers.parse("A Kill Chain Phase is created."))
def when_kill_chain_phase_stix21_constraint_kill_chain_name(
    context,
):
    kill_chain_name = {}
    try:
        kill_chain_name = json.loads(context["kill_chain_name"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_kill_chain_name(kill_chain_name)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A ValueError should be raised, stating that the kill_chain_name must be lowercase with hyphens."
    )
)
def then_kill_chain_phase_stix21_constraint_kill_chain_name(
    context,
):
    assert type(context["error"]) is ValueError
    assert (
        str(context["error"])
        == "`kill_chain_name` must be a str in lowercase with hyphens."
    )
