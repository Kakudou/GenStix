import os

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
    "/constraints/gen_stix/cdts/kill_chain_phase/kill_chain_phase_stix21_required_phase_name.constraint",
    "Creating a Kill Chain Phase without a phase_name.",
)
def test_kill_chain_phase_stix21_required_phase_name():
    pass


@given(
    parsers.parse(
        "A Kill Chain Phase is created without a {phase_name} and a valid {kill_chain_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_stix21_required_phase_name(
    phase_name, kill_chain_name
):
    input_contract = (
        CreateKillChainPhaseInputPortBuilder()
        .create()
        .with_kill_chain_name(kill_chain_name)
    )

    return {"input_contract": input_contract}


@when(parsers.parse("A Kill Chain Phase is created."))
def when_kill_chain_phase_stix21_required_phase_name(
    context,
):
    try:
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A ValueError should be raised, stating that the phase_name is required."
    )
)
def then_kill_chain_phase_stix21_required_phase_name(
    context,
):
    assert type(context["error"]) is ValueError
    assert (
        str(context["error"])
        == "`phase_name` is a required field for KillChainPhase"
    )
