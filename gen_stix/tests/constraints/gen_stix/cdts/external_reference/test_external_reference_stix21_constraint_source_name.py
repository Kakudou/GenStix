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
    "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_constraint_source_name.constraint",
    "Creating an ExternalReference with an invalid source_name.",
)
def test_external_reference_stix21_constraint_source_name():
    pass


@given(
    parsers.parse(
        "An ExternalReference is created with an invalid {source_name}."
    ),
    target_fixture="context",
)
def given_external_reference_stix21_constraint_source_name(source_name):
    input_contract = CreateExternalReferenceInputPortBuilder().create()

    return {"source_name": source_name, "input_contract": input_contract}


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_constraint_source_name(
    context,
):
    source_name = {}
    try:
        source_name = json.loads(context["source_name"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_source_name(source_name)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A TypeError should be raised, stating that {source_name} must be a string."
    )
)
def then_external_reference_stix21_constraint_source_name(
    context, source_name
):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`source_name` must be a str."
