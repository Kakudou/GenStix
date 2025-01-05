import os
import json

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers


from gen_stix.src.utils.container import Container

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder import (
    CreateAttackPatternInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.create_external_reference.create_external_reference_inputport_builder import (
    CreateExternalReferenceInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_inputport_builder import (
    CreateKillChainPhaseInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_optional_fields.constraint",
    "Creating an AttackPattern with all or some optional fields filled.",
)
def test_attack_pattern_stix21_optional_fields():
    pass


@given(
    parsers.parse(
        "An AttackPattern is created with {external_references}, {description}, {aliases}, {kill_chain_phases}, a {name}, and a {type_}."
    ),
    target_fixture="context",
)
def given_attack_pattern_stix21_optional_fields(
    external_references, description, aliases, kill_chain_phases, name, type_
):
    list_eref = []
    for external_ref in json.loads(external_references):
        eref_contract = (
            CreateExternalReferenceInputPortBuilder()
            .create()
            .with_source_name(external_ref["source_name"])
            .with_description(external_ref["description"])
            .build()
        )
        eref_usecase = Container.get_usecase_repo(
            "CreateExternalReference", STORAGE_ENGINE
        )
        eref_contract = eref_usecase.execute(eref_contract)
        if eref_contract.error is None:
            list_eref.append(
                {
                    "source_name": eref_contract.source_name,
                    "description": eref_contract.description,
                    "external_id": eref_contract.external_id,
                }
            )

    list_kchain = []
    for kill_chain_phase in json.loads(kill_chain_phases):
        kchain_contract = (
            CreateKillChainPhaseInputPortBuilder()
            .create()
            .with_kill_chain_name(kill_chain_phase["kill_chain_name"])
            .with_phase_name(kill_chain_phase["phase_name"])
            .build()
        )
        kchain_usecase = Container.get_usecase_repo(
            "CreateKillChainPhase", STORAGE_ENGINE
        )
        kchain_contract = kchain_usecase.execute(kchain_contract)
        if kchain_contract.error is None:
            list_kchain.append(
                {
                    "kill_chain_name": kchain_contract.kill_chain_name,
                    "phase_name": kchain_contract.phase_name,
                }
            )

    input_contract = (
        CreateAttackPatternInputPortBuilder()
        .create()
        .with_external_references(list_eref)
        .with_description(description)
        .with_aliases(json.loads(aliases))
        .with_kill_chain_phases(list_kchain)
        .with_name(name)
        .with_type_(type_)
        .build()
    )

    return {
        "list_eref": list_eref,
        "list_kchain": list_kchain,
        "input_contract": input_contract,
    }


@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_optional_fields(context):
    usecase = Container.get_usecase_repo("CreateAttackPattern", STORAGE_ENGINE)
    output_contract = usecase.execute(context["input_contract"])
    context["output_contract"] = output_contract


@then(
    parsers.parse(
        "The fields {external_references}, {description}, {aliases}, {kill_chain_phases}, {name}, and {type_} should match the input values."
    )
)
def then_attack_pattern_stix21_optional_fields(
    context,
    external_references,
    description,
    aliases,
    kill_chain_phases,
    name,
    type_,
):
    assert (
        context["output_contract"].external_references == context["list_eref"]
    )
    assert context["output_contract"].description == description
    assert context["output_contract"].aliases == json.loads(aliases)
    assert (
        context["output_contract"].kill_chain_phases == context["list_kchain"]
    )
    assert context["output_contract"].name == name
    assert context["output_contract"].type_ == type_
