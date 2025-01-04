import os
import json

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.src.gen_stix.usecase.\
     cdts.external_reference.create_external_reference.create_external_reference_inputport_builder\
     import CreateExternalReferenceInputPortBuilder


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_constraint_url.constraint",
          "Creating an ExternalReference with an invalid url.")
def test_external_reference_stix21_constraint_url():
    pass


@given(parsers.parse("An ExternalReference is created with {source_name} and an invalid {url}."), target_fixture="context")
def given_external_reference_stix21_constraint_url(source_name, url):
    input_contract = CreateExternalReferenceInputPortBuilder()\
        .create()\
        .with_source_name(source_name)

    return {
        "url": url,
        "input_contract": input_contract
    }


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_constraint_url(context, ):
    url = {}
    try:
        url = json.loads(context["url"])
    except json.JSONDecodeError:
        pass
    try:
        context["input_contract"].with_url(url)
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(parsers.parse("A ValueError should be raised, stating that {url} must conform to RFC3986."))
def then_external_reference_stix21_constraint_url(context, url):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`url` must be a str."
