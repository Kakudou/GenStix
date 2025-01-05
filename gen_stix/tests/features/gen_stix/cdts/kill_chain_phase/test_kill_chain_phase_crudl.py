import os

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers

from gen_stix.src.utils.container import Container

from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_inputport_builder import (
    CreateKillChainPhaseInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.update_kill_chain_phase.update_kill_chain_phase_inputport_builder import (
    UpdateKillChainPhaseInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_inputport_builder import (
    DeleteKillChainPhaseInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/features/gen_stix/cdts/kill_chain_phase/kill_chain_phase_crudl.feature",
    "Performing CRUDL operations on a STIX 2.1 Kill Chain Phase.",
)
def test_kill_chain_phase_crudl():
    pass


@given(
    parsers.parse(
        "A Kill Chain Phase is created with {kill_chain_name} and {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_crudl(kill_chain_name, phase_name):
    input_contract = (
        CreateKillChainPhaseInputPortBuilder()
        .create()
        .with_kill_chain_name(kill_chain_name)
        .with_phase_name(phase_name)
        .build()
    )

    return {
        "kill_chain_name": kill_chain_name,
        "phase_name": phase_name,
        "input_contract": input_contract,
    }


@when(parsers.parse("The Kill Chain Phase is created, updated, and deleted."))
def when_kill_chain_phase_crudl(
    context,
):
    usecase = Container.get_usecase_repo(
        "CreateKillChainPhase", STORAGE_ENGINE
    )
    create_contract = usecase.execute(context["input_contract"])

    if "updated" in context["phase_name"]:
        input_contract = (
            UpdateKillChainPhaseInputPortBuilder()
            .create()
            .with_kill_chain_name(context["kill_chain_name"])
            .with_phase_name(context["phase_name"])
            .build()
        )
        usecase = Container.get_usecase_repo(
            "UpdateKillChainPhase", STORAGE_ENGINE
        )
        update_contract = usecase.execute(input_contract)
        output_contract = update_contract
    elif "deleted" in context["phase_name"]:
        input_contract = (
            DeleteKillChainPhaseInputPortBuilder()
            .create()
            .with_kill_chain_name(context["kill_chain_name"])
            .with_phase_name(context["phase_name"])
            .build()
        )
        usecase = Container.get_usecase_repo(
            "DeleteKillChainPhase", STORAGE_ENGINE
        )
        delete_contract = usecase.execute(input_contract)
        output_contract = delete_contract
    else:
        output_contract = create_contract

    context["output_contract"] = output_contract


@then(
    parsers.parse(
        "A Kill Chain Phase should exist with {kill_chain_name} and {phase_name}, and one Kill Chain Phase should be deleted."
    )
)
def then_kill_chain_phase_crudl(context, kill_chain_name, phase_name):
    if "deleted" not in phase_name:
        assert context["output_contract"].kill_chain_name == kill_chain_name
        assert context["output_contract"].phase_name == phase_name
    else:
        assert context["output_contract"].deleted is True
