import os

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers


from gen_stix.src.utils.container import Container

from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_inputport_builder import (
    CreateKillChainPhaseInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/constraints/gen_stix/cdts/kill_chain_phase/kill_chain_phase_check_unicity_by_phase_name_kill_chain_name.constraint",
    "Creating multiple Kill Chain Phases with the same kill_chain_name and phase_name.",
)
def test_kill_chain_phase_check_unicity_by_phase_name_kill_chain_name():
    pass


@given(
    parsers.parse(
        "Multiple Kill Chain Phases are created with the same {kill_chain_name} and {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_check_unicity_by_phase_name_kill_chain_name(
    kill_chain_name, phase_name
):
    input_contract_1 = (
        CreateKillChainPhaseInputPortBuilder()
        .create()
        .with_kill_chain_name(kill_chain_name)
        .with_phase_name(phase_name)
        .build()
    )

    input_contract_2 = (
        CreateKillChainPhaseInputPortBuilder()
        .create()
        .with_kill_chain_name(kill_chain_name)
        .with_phase_name(phase_name)
        .build()
    )

    return {
        "input_contract_1": input_contract_1,
        "input_contract_2": input_contract_2,
    }


@when(parsers.parse("A Kill Chain Phase is created."))
def when_kill_chain_phase_check_unicity_by_phase_name_kill_chain_name(
    context,
):
    usecase = Container.get_usecase_repo(
        "CreateKillChainPhase", STORAGE_ENGINE
    )
    usecase.execute(context["input_contract_1"])
    create_contract = usecase.execute(context["input_contract_2"])

    context["output_contract"] = create_contract


@then(
    parsers.parse(
        "A NameError exception should be raised with the message 'The Kill Chain Phase you want already exists'."
    )
)
def then_kill_chain_phase_check_unicity_by_phase_name_kill_chain_name(
    context,
):
    assert (
        context["output_contract"].error
        == "The KillChainPhase you want, already exist"
    )
