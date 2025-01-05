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
    "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_constraint_description.constraint",
    "Creating an ExternalReference with an invalid description.",
)
def test_external_reference_stix21_constraint_description():
    pass


@given(
    parsers.parse(
        "An ExternalReference is created with {source_name} and invalid {description}."
    ),
    target_fixture="context",
)
def given_external_reference_stix21_constraint_description(
    source_name, description
):
    input_contract = (
        CreateExternalReferenceInputPortBuilder()
        .create()
        .with_source_name(source_name)
    )

    return {"description": description, "input_contract": input_contract}


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_constraint_description(
    context,
):
    description = {}
    try:
        description = json.loads(context["description"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_description(description)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A TypeError should be raised, stating that {description} must be a string."
    )
)
def then_external_reference_stix21_constraint_description(
    context, description
):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`description` must be a str."
