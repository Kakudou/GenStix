import os
import json

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.src.utils.container\
    import Container

from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_inputport_builder\
    import CreateExternalReferenceInputPortBuilder

from gen_stix.src.gen_stix.entity.\
    enums.external_reference_capec\
    import ExternalReferenceCapec


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_optional_fields.constraint",
          "Creating an ExternalReference with all or some of the optional fields populated.")
def test_external_reference_stix21_optional_fields():
    pass


@given(parsers.parse("An ExternalReference is created with {source_name}, {description}, {url}, {hashes}, and {external_id}."), target_fixture="context")
def given_external_reference_stix21_optional_fields(source_name, description, url, hashes, external_id):
    if source_name == "capec":
        wanted_external_id = f"CAPEC-{ExternalReferenceCapec.from_name(description).value}"
    else:
        wanted_external_id = external_id
    input_contract = CreateExternalReferenceInputPortBuilder()\
        .create()\
        .with_source_name(source_name)\
        .with_description(description)\
        .with_url(url)\
        .with_hashes(json.loads(hashes))\
        .with_external_id(wanted_external_id)\
        .build()

    return {
        "external_id": wanted_external_id,
        "input_contract": input_contract
    }


@when(parsers.parse("The ExternalReference is created with optional fields."))
def when_external_reference_stix21_optional_fields(context, ):
    usecase = Container.get_usecase_repo("CreateExternalReference", STORAGE_ENGINE)
    output_contract = usecase.execute(context["input_contract"])
    context["output_contract"] = output_contract


@then(parsers.parse("The fields {description}, {url}, {hashes}, and {external_id} of the object should be as provided during creation."))
def then_external_reference_stix21_optional_fields(context, description, url, hashes, external_id):
    assert context["output_contract"]\
        .description == description
    assert context["output_contract"]\
        .url == url
    assert context["output_contract"]\
        .hashes == json.loads(hashes)
    assert context["output_contract"]\
        .external_id == context["external_id"]
