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
    "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_constraint_hashes.constraint",
    "Creating an ExternalReference with invalid hashes or missing a SHA-256 hash when a URL is present.",
)
def test_external_reference_stix21_constraint_hashes():
    pass


@given(
    parsers.parse(
        "An ExternalReference is created with {source_name} and invalid {hashes}."
    ),
    target_fixture="context",
)
def given_external_reference_stix21_constraint_hashes(source_name, hashes):
    input_contract = (
        CreateExternalReferenceInputPortBuilder()
        .create()
        .with_source_name(source_name)
    )

    return {"hashes": hashes, "input_contract": input_contract}


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_constraint_hashes(
    context,
):
    hashes = ""
    try:
        hashes = json.loads(context["hashes"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_hashes(hashes)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(
    parsers.parse(
        "A ValueError should be raised, stating that {hashes} must be a valid dictionary of hashes with SHA-256 included when possible."
    )
)
def then_external_reference_stix21_constraint_hashes(context, hashes):
    assert type(context["error"]) is ValueError
    assert (
        str(context["error"]) == "`hashes` must be a Dict."
        or str(context["error"]) == "`hashes` key must be an HashesOV."
        or str(context["error"]).startswith("No hashes-ov found for ")
    )
