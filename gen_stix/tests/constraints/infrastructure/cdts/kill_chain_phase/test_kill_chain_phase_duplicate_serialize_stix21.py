import os

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
    "/constraints/infrastructure/cdts/kill_chain_phase/kill_chain_phase_duplicate_serialize_stix21.constraint",
    "Serialize multiple time a Kill Chain Phase Core Object, and ensure only one stix2.1 is created.",
)
def test_kill_chain_phase_duplicate_serialize_stix21():
    pass


@given(
    parsers.parse(
        "I create a Kill Chain Phase with {kill_chain_name} and {phase_name}."
    ),
    target_fixture="context",
)
def given_kill_chain_phase_duplicate_serialize_stix21(
    kill_chain_name, phase_name
):
    inputs = {}
    inputs["kill_chain_name"] = kill_chain_name
    inputs["phase_name"] = phase_name
    kill_chain = CreateKillChainPhaseAdapter.execute(inputs, STORAGE_ENGINE)
    print(kill_chain)

    return {
        "kill_chain": kill_chain,
    }


@when(parsers.parse("I serialize that object two times into STIX2.1."))
def when_kill_chain_phase_duplicate_serialize_stix21(
    context,
):
    kill_chain = context["kill_chain"]
    kill_chain_phase_dto = KillChainPhaseDTO()
    kill_chain_phase_dto.kill_chain_name = kill_chain.kill_chain_name
    kill_chain_phase_dto.phase_name = kill_chain.phase_name
    context["stix21_1"] = kill_chain_phase_dto.to_stix21()
    context["stix21_2"] = kill_chain_phase_dto.to_stix21()


@then(
    parsers.parse(
        "I should get the exact same stix2.1 object and no duplicate."
    )
)
def then_kill_chain_phase_duplicate_serialize_stix21(context):
    assert context["stix21_1"] == context["stix21_2"]
