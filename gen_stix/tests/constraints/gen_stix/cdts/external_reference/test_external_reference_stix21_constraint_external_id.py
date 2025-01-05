import os
import json

from pytest import mark
from pytest_bdd import scenario, given, when, then, parsers


from gen_stix.src.gen_stix.usecase.cdts.external_reference.create_external_reference.create_external_reference_inputport_builder import (
    CreateExternalReferenceInputPortBuilder,
)


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(
    f"{__fullpath.split('/GenSTIX/')[0]}"
    "/GenSTIX/gen_stix"
    "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_constraint_external_id.constraint",
    "Creating an ExternalReference with an invalid external_id.",
)
def test_external_reference_stix21_constraint_external_id():
    pass


@given(
    parsers.parse(
        "An ExternalReference is created with {source_name} and an invalid {external_id}."
    ),
    target_fixture="context",
)
def given_external_reference_stix21_constraint_external_id(
    source_name, external_id
):
    input_contract = (
        CreateExternalReferenceInputPortBuilder()
        .create()
        .with_source_name(source_name)
    )

    return {"external_id": external_id, "input_contract": input_contract}


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_constraint_external_id(
    context,
):
    external_id = {}
    try:
        external_id = json.loads(context["external_id"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_external_id(external_id)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A TypeError should be raised, stating that {external_id} must be a string."
    )
)
def then_external_reference_stix21_constraint_external_id(
    context, external_id
):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`external_id` must be a str."
