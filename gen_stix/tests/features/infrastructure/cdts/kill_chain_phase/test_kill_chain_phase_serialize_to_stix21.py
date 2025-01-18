import os

from json import loads as json_loads
from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers

from gen_stix.src.app.adapter.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_adapter import (
    CreateKillChainPhaseAdapter,
)
from gen_stix.src.app.dto.cdts.kill_chain_phase.kill_chain_phase_dto import (
    KillChainPhaseDTO,
)

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/features/infrastructure/cdts/kill_chain_phase/kill_chain_phase_serialize_to_stix21.feature",
    "Serialize an existing Kill Chain Phase Core object into a valid STIX2.1 object and check the json.",
)
def test_kill_chain_phase_serialize_to_stix21():
    pass


@given(
    parsers.parse(
        "I create a Kill Chain Phase with {kill_chain_name} and {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_serialize_to_stix21(kill_chain_name, phase_name):
    inputs = {}
    inputs["kill_chain_name"] = kill_chain_name
    inputs["phase_name"] = phase_name
    kill_chain = CreateKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)

    return {
        "kill_chain": kill_chain,
    }


@when(parsers.parse("I serialize that object into STIX2.1"))
def when_kill_chain_phase_serialize_to_stix21(context):
    kill_chain = context["kill_chain"]
    kill_chain_phase_dto = KillChainPhaseDTO()
    kill_chain_phase_dto.kill_chain_name = kill_chain.kill_chain_name
    kill_chain_phase_dto.phase_name = kill_chain.phase_name
    context["stix21"] = kill_chain_phase_dto.to_stix21()


@then(
    parsers.parse(
        "I should be able to get the {valid_stix21} json for that object."
    )
)
def then_kill_chain_phase_serialize_to_stix21(context, valid_stix21):
    assert context["stix21"] == json_loads(valid_stix21)
