import os

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers

from gen_stix.src.app.adapter.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_adapter import (
    CreateKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_adapter import (
    ListKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.read_kill_chain_phase.read_kill_chain_phase_adapter import (
    ReadKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_adapter import (
    DeleteKillChainPhaseAdapter,
)

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist


STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/features/infrastructure/cdts/kill_chain_phase/kill_chain_phase_infile_crudl.feature",
    "Performing CRUDL operations on a STIX2.1 Kill Chain Phase.",
)
def test_kill_chain_phase_infile_crudl():
    pass


@given(
    parsers.parse(
        "A Kill Chain Phase is created with {kill_chain_name} and {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_infile_crudl(kill_chain_name, phase_name):
    InFilePersist().save_path = "/tmp/GenStix/pytests"

    inputs = {}

    list_number = len(
        ListKillChainPhaseAdapter.execute(
            inputs, STORAGE_ENGINE
        ).all_kill_chain_phases
    )

    inputs["kill_chain_name"] = kill_chain_name
    inputs["phase_name"] = phase_name
    kill_chain = CreateKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)

    return {
        "kill_chain_name": kill_chain_name,
        "phase_name": phase_name,
        "list_number": list_number + 1,
        "kill_chain": kill_chain,
    }


@when(
    parsers.parse(
        "The Kill Chain Phase is create, read, update, list and deleted."
    )
)
def when_kill_chain_phase_infile_crudl(context):
    if context["kill_chain"].kill_chain_name.startswith("delete"):
        inputs = {}
        inputs["kill_chain_name"] = context["kill_chain"].kill_chain_name
        inputs["phase_name"] = context["kill_chain"].phase_name
        DeleteKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)
        context["list_number"] -= 1


@then(
    parsers.parse(
        "The Kill Chain Phase should be retrieve from the file if exists."
    )
)
def then_kill_chain_phase_infile_crudl(context):
    inputs = {}
    inputs["kill_chain_name"] = context["kill_chain_name"]
    inputs["phase_name"] = context["phase_name"]
    assert context["list_number"] == len(
        ListKillChainPhaseAdapter.execute(
            {}, STORAGE_ENGINE
        ).all_kill_chain_phases
    )
    if context["kill_chain_name"].startswith("delete"):
        assert (
            ReadKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE).error
            == "This KillChainPhase, doesn't look like to exist"
        )
    else:
        kill_chain = ReadKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)
        assert (
            context["kill_chain"].kill_chain_name == kill_chain.kill_chain_name
        )
        assert context["kill_chain"].phase_name == kill_chain.phase_name
        DeleteKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)
