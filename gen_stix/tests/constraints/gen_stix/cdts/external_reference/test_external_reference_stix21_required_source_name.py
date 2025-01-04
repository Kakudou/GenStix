import os

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
          "/constraints/gen_stix/cdts/external_reference/external_reference_stix21_required_source_name.constraint",
          "Creating an ExternalReference without a source_name.")
def test_external_reference_stix21_required_source_name():
    pass


@given(parsers.parse("An ExternalReference is created without a {source_name}."), target_fixture="context")
def given_external_reference_stix21_required_source_name(source_name):
    input_contract = CreateExternalReferenceInputPortBuilder()\
        .create()

    return {
        "input_contract": input_contract
    }


@when(parsers.parse("The ExternalReference is created."))
def when_external_reference_stix21_required_source_name(context, ):
    try:
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(parsers.parse("A ValueError should be raised, stating that {source_name} is required."))
def then_external_reference_stix21_required_source_name(context, source_name):
    assert type(context["error"]) is ValueError
    assert str(context["error"]) == "`source_name` is a required field for ExternalReference"
