import os

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.src.utils.container\
    import Container

from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_inputport_builder\
    import CreateExternalReferenceInputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.update_external_reference.update_external_reference_inputport_builder\
    import UpdateExternalReferenceInputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.delete_external_reference.delete_external_reference_inputport_builder\
    import DeleteExternalReferenceInputPortBuilder


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/features/gen_stix/cdts/external_reference/external_reference_crudl.feature",
          "Performing CRUDL operations on a STIX 2.1 ExternalReference.")
def test_external_reference_crudl():
    pass


@given(parsers.parse("An ExternalReference is created with {source_name}, {description}."), target_fixture="context")
def given_external_reference_crudl(source_name, description):
    input_contract = CreateExternalReferenceInputPortBuilder()\
        .create()\
        .with_source_name(source_name)\
        .with_description(description)\
        .build()

    return {
        "source_name": source_name,
        "description": description,
        "input_contract": input_contract
    }


@when(parsers.parse("The ExternalReference is created, updated with {new_description} and deleted."))
def when_external_reference_crudl(context, new_description):
    usecase = Container.get_usecase_repo("CreateExternalReference", STORAGE_ENGINE)
    create_contract = usecase.execute(context["input_contract"])

    if "Updated" in new_description:
        input_contract = UpdateExternalReferenceInputPortBuilder()\
            .create()\
            .with_source_name(context["source_name"])\
            .with_description(new_description)\
            .with_external_id(create_contract.external_id)\
            .build()
        usecase = Container.get_usecase_repo("UpdateExternalReference", STORAGE_ENGINE)
        update_contract = usecase.execute(input_contract)
        output_contract = update_contract
    elif "Deleted" in new_description:
        input_contract = DeleteExternalReferenceInputPortBuilder()\
            .create()\
            .with_source_name(context["source_name"])\
            .with_external_id(create_contract.external_id)\
            .build()
        usecase = Container.get_usecase_repo("DeleteExternalReference", STORAGE_ENGINE)
        delete_contract = usecase.execute(input_contract)
        output_contract = delete_contract
    else:
        output_contract = create_contract

    context["output_contract"] = output_contract


@then(parsers.parse("An ExternalReference should exist with {new_description}, and {source_name}, and one ExternalReference should be deleted."))
def then_external_reference_crudl(context, new_description, source_name):
    if "Deleted" not in new_description:
        assert context["output_contract"]\
            .source_name == source_name
        assert context["output_contract"]\
            .description == new_description
    else:
        assert context["output_contract"]\
            .deleted is True
