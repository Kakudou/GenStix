import os

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers

from gen_stix.src.utils.container import Container

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder import (
    CreateAttackPatternInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.update_attack_pattern.update_attack_pattern_inputport_builder import (
    UpdateAttackPatternInputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_inputport_builder import (
    DeleteAttackPatternInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/features/gen_stix/sdos/attack_pattern/attack_pattern_crudl.feature",
    "Performing CRUDL operations on a STIX 2.1 AttackPattern.",
)
def test_attack_pattern_crudl():
    pass


@given(
    parsers.parse(
        "An AttackPattern is created with {type_}, {name}, and {description}."
    ),
    target_fixture="context",
)
def given_attack_pattern_crudl(type_, name, description):
    input_contract = (
        CreateAttackPatternInputPortBuilder()
        .create()
        .with_type_(type_)
        .with_name(name)
        .with_description(description)
        .build()
    )

    return {
        "type_": type_,
        "name": name,
        "description": description,
        "input_contract": input_contract,
    }


@when(
    parsers.parse(
        "The AttackPattern is created, updated with {new_description}, and deleted."
    )
)
def when_attack_pattern_crudl(context, new_description):
    usecase = Container.get_usecase_repo("CreateAttackPattern", STORAGE_ENGINE)
    create_contract = usecase.execute(context["input_contract"])

    if "Updated" in new_description:
        input_contract = (
            UpdateAttackPatternInputPortBuilder()
            .create()
            .with_type_(context["type_"])
            .with_name(context["name"])
            .with_description(new_description)
            .build()
        )
        usecase = Container.get_usecase_repo(
            "UpdateAttackPattern", STORAGE_ENGINE
        )
        update_contract = usecase.execute(input_contract)
        output_contract = update_contract
    elif "Deleted" in new_description:
        input_contract = (
            DeleteAttackPatternInputPortBuilder()
            .create()
            .with_type_(context["type_"])
            .with_name(context["name"])
            .build()
        )
        usecase = Container.get_usecase_repo(
            "DeleteAttackPattern", STORAGE_ENGINE
        )
        delete_contract = usecase.execute(input_contract)
        output_contract = delete_contract
    else:
        output_contract = create_contract

    context["output_contract"] = output_contract


@then(
    parsers.parse(
        "An AttackPattern should exist with {new_description}, {name}, and {type_}, and one AttackPattern should be deleted."
    )
)
def then_attack_pattern_crudl(context, new_description, name, type_):
    if "Deleted" not in new_description:
        assert context["output_contract"].type_ == type_
        assert context["output_contract"].name == name
        assert context["output_contract"].description == new_description
    else:
        assert context["output_contract"].deleted is True
