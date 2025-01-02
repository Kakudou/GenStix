import os

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.src.utils.container\
    import Container

from gen_stix.src.gen_stix.usecase.\
     sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder\
     import CreateAttackPatternInputPortBuilder

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_check_unicity_by_type_name.constraint",
          "Creating multiple AttackPatterns with the same name and type.")
def test_attack_pattern_check_unicity_by_type_name():
    pass


@given(parsers.parse("Multiple AttackPatterns are created with the same {name} and {type_}."), target_fixture="context")
def given_attack_pattern_check_unicity_by_type_name(name, type_):
    input_contract_1 = CreateAttackPatternInputPortBuilder()\
        .create()\
        .with_name(name)\
        .with_type_(type_)\
        .build()

    input_contract_2 = CreateAttackPatternInputPortBuilder()\
        .create()\
        .with_name(name)\
        .with_type_(type_)\
        .build()

    return {
        "input_contract_1": input_contract_1,
        "input_contract_2": input_contract_2
    }


@when(parsers.parse("An AttackPattern is created."))
def when_attack_pattern_check_unicity_by_type_name(context):
    usecase = Container.get_usecase_repo("CreateAttackPattern", STORAGE_ENGINE)
    usecase.execute(context["input_contract_1"])
    create_contract = usecase.execute(context["input_contract_2"])

    context["output_contract"] = create_contract


@then(parsers.parse("A NameError exception should be raised with the message 'The AttackPattern you want, already exists'."))
def then_attack_pattern_check_unicity_by_type_name(context):
    assert context["output_contract"].error == "The AttackPattern you want, already exist"
