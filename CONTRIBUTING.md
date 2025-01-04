# **GenSTIX Contributing Guide**

---

## **TL;DR**

---

###  **Workflow for a New Feature**

---

#### **Plan and Define Behavior**

Identify the feature's scope and purpose.
Write Gherkin feature files using BDD syntax (Given, When, Then).
Add constraints to define the rules for validation and business logic.

---

#### **Write Unit Tests First (TDD)**

Create pytest test cases to cover all edge cases and expected behaviors, including constraints.
Run tests to ensure they fail before writing the feature code.

---

#### **Develop the Core Logic**

##### **Entity Creation**

Implement or update the relevant domain entity to represent the feature concept (e.g., AttackPattern).

##### **Use Case Implementation**

Write the use case logic that orchestrates the feature's behavior and enforces constraints.

##### **Validate Input**

Add an input validator to ensure inputs align with the expected schema and rules.

#### **Integrate Behavior Tests (BDD)**

Run Gherkin scenarios as integration tests to ensure the feature works as expected in a complete flow.

#### **Refactor and Test**

Refactor code for clarity, modularity, and compliance with Clean Architecture principles.
Ensure all tests pass (pytest).

#### **Document the Feature**

Update or create documentation for the feature (e.g., CLI usage, API calls, examples).

#### **Submit for Review**

Rebase your branch with the latest main.
Check for consistency, correctness, and adherence to project standards.
Submit a pull request with a clear description of the changes and test coverage.

#### **Pull Request Process**

Checklist Before Opening a PR:

  - [ ] Ensure your feature branch is rebased with the latest main.
  - [ ] Double-check that all unit tests and integration tests pass (pytest).
  - [ ] Verify documentation is updated and correctly describes the new feature.
  - [ ] Use meaningful commit messages with gitmoji, and squash unnecessary commits.

#### **Submit the Pull Request**

Include a clear description of the changes.
Provide a summary of the feature, behavior, and purpose.
Attach test results or relevant screenshots if needed.
Add reviewers and labels (e.g., feature, bugfix).

#### **Respond to Feedback**

Address code review comments promptly.
Make iterative changes as requested and rebase if necessary.

---

### **General Guidelines**

Always follow Clean Architecture principles and adhere to TDD/BDD workflows.
Write clean, modular, and testable code.
Respect feedback and iterate quickly on reviews.

---

### **Environment Setup**

Clone the Repository:

```bash
git clone https://github.com/kakudou/GenStix.git
cd GenSTIX
```

Install Dependencies:

```bash
python -m venv .venv --prompt=GenSTIX
source .venv/bin/activate
python -m pip install -e .[dev]
```

Run Tests:

```bash
pytest
```

---

### **Branching Strategy**
Create a Feature Branch:

```bash
git checkout -b feature/<your-feature-name>
```

---

### **Commit and Push**

Use clear and atomic commits, bonuses for gitmoji usage.

```bash
git commit -m ":sparkles: Add feature XYZ"
git push origin feature/<your-feature-name>
```

---

### **Code Standards**

Follow PEP 8 for Python coding style.
Write clear and concise docstrings for every module, class, and function.
Use type hints to maintain code readability and consistency.

---

### **Documentation Requirements**

Include a description of the feature, its purpose, and examples of usage.
Document any new CLI commands, API endpoints, or configuration options.
Ensure documentation is easy to follow for new contributors or users.

Treat documentation as a core part of the feature and separate commit updates from your code.

---

### **Examples and Tutorials**

Provide example workflows, Gherkin files, or usage instructions in README or other docs.

---

## Detailed Contributing Guide

I'm using my own custom framework, [BoilerplateGenerator](https://github.com/kakudou/BoilerplateGenerator.git), to generate most of the boilerplate classes. Feel free to use it if you'd like, or create everything manually. My example will involve the usage of that tool.

### The Goals
First, we need to identify the goals we want to achieve. To do so, let's think in human terms instead of technical ones.


```
I would like to be able to create a stix2.1 object who will be an AttackPattern. I want that object to respect all the rules of the associated stix2.1 object. And i need to be able to export it as a json for futher usages.
It would be pretty usefull to have a way to update it and seeing all already created AttackPattern.
If the tools can handle the fact i don't want to have duplicate entries, it would be awesome !
```

### Identify Features an Constraints

As you can see, I've described what I want without focusing on implementation details or the technology behind it. Now, it's time to translate those goals into features and constraints using a Gherkin-style approach.

This is an important step because we are working with Behavior-Driven Development (BDD). You shouldn't start developing anything until you have tests ready for it. I find Gherkin to be a really good method for creating atomic requirements.

Let's identify the features:

1) attack_pattern_crudl: We need to be able to perform CRUDL operations on AttackPattern (I've intentionally combined this into one feature, as my framework allows me to generate an all-in-one solution).
2) attack_pattern_export_json: We need to be able to export the AttackPattern as JSON.

Now, for the constraints:

1) attack_pattern_stix21_required_<field>: Ensures the AttackPattern includes the required fields from the STIX 2.1 definition.
2) attack_pattern_stix21_optional_fields: Ensures that optional fields from the STIX 2.1 definition can be included.
3) attack_pattern_check_unicity_by_<fields>: Ensures that duplicates are not created for the same AttackPattern.
4) attack_pattern_stix21_constraint_<field>: Ensures that fields follow the constraints as described in the STIX 2.1 definition.
As you can see, we can't list all the constraints at this point, since we don’t yet know the fields involved in our object.

### Gather complementary informations

To properly define our features and constraints, we need to check the STIX 2.1 specification for AttackPattern. We gather this data from:
[AttackPattern definition](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_axjijf603msy)

|**Property Name**|**Type**|**Description**|
|---|---|---|
|**type** (required)|string|The value of this property **MUST** be attack-pattern.|
|**external_references**<br><br>(optional)|list of type external-reference|A list of external references which refer to non-STIX information. This property **MAY** be used to provide one or more Attack Pattern identifiers, such as a CAPEC ID. When specifying a CAPEC ID, the **source_name** property of the external reference **MUST** be set to capec and the **external_id** property **MUST** be formatted as CAPEC-[id].|
|**name** (required)|string|A name used to identify the Attack Pattern.|
|**description** (optional)|string|A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.|
|**aliases** (optional)|list of type string|Alternative names used to identify this Attack Pattern.|
|**kill_chain_phases** (optional)|list of type kill-chain-phase|The list of Kill Chain Phases for which this Attack Pattern is used.|

With this information, we can now create the scenarios for our features and constraints.

Features: 
- attack_pattern_crudl
- attack_pattern_export_json

Constraints: 
- attack_pattern_stix21_required_type
- attack_pattern_stix21_required_name
- attack_pattern_stix2.1_constraint_type
- attack_pattern_stix2.1_constraint_name
- attack_pattern_check_unicity_by_type_name
- attack_pattern_stix21_optional_fields
- attack_pattern_stix2.1_constraint_external_references
- attack_pattern_stix2.1_constraint_description
- attack_pattern_stix2.1_constraint_aliases
- attack_pattern_stix2.1_constraint_kill_chain_phases

### Let's do some code, maybe...

Now that we have all the necessary information, let's start coding. As mentioned earlier, I will be using my framework, [BoilerplateGenerator](https://github.com/kakudou/BoilerplateGenerator.git), so most of the code is generated for us. I'll focus on the constraints and non-CRUDL use cases.

#### First Feature: attack_pattern_crudl

We are going to create the feature attack_pattern_crudl. Let's use BoilerplateGenerator to do that.

```bash
$ BoilerplateGenerator create-feature
let's create a new feature
? Select one project in all of that: GenSTIX
? What's the name of the feature ? AttackPatternCrudl
? What types of feature this will be? core
? What's the feature domain? sdos/attack_pattern
? Can you describe the feature? CRUDL for the STIX 2.1 object AttackPattern.
? Can you describe the scenario? Performing CRUDL operations on a STIX 2.1 AttackPattern.
? Can you describe the 'Given' of that scenario? An AttackPattern is created with <type_>, <name>, and <description>.
? Can you describe the 'When' of that scenario? The AttackPattern is created, updated with <new_description>, and deleted.
? Can you describe the 'Then' of that scenario? An AttackPattern should exist with <new_description>, <name>, and <type_>, and one AttackPatter
n should be deleted.

? Are you sure of the above inputs? Yes
The feature AttackPatternCrudl has been created.
```

This will create a YAML file `GenStix.yml`. Now, let's generate the associated class and code:

```bash
$ BoilerplateGenerator generate-feature
let's generate a feature
? Select one project in all of that: GenSTIX
? Select one feature in all of that: AttackPatternCrudl
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/features/gen_stix/sdos/attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/tests/features/gen_stix/sdos/attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/features/gen_stix/sdos/attack_pattern/attack_pattern_crudl.feature
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/tests/features/gen_stix/sdos/attack_pattern/test_attack_pattern_crudl.py
```

The following files will be created:
 - /home/kakudou/construct/python/WiP/GenSTIX/gen_stix/features/gen_stix/sdos/attack_pattern/attack_pattern_crudl.feature
 - /home/kakudou/construct/python/WiP/GenSTIX/gen_stix/tests/features/gen_stix/sdos/attack_pattern/test_attack_pattern_crudl.py

The generated .feature and .py files will look like this:

1) attack_pattern_crudl.feature

```gherkin
Feature: CRUDL for the STIX 2.1 object AttackPattern.

    Scenario Outline: Performing CRUDL operations on a STIX 2.1 AttackPattern.
        Given An AttackPattern is created with <type_>, <name>, and <description>.
        When The AttackPattern is created, updated with <new_description>, and deleted.
        Then An AttackPattern should exist with <new_description>, <name>, and <type_>, and one AttackPattern should be deleted.

        Examples:
            | |
            | |
```

2) test_attack_pattern_crudl.py

```python
import os

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers

from gen_stix.tests.factory\
    import Factory

from gen_stix.src.utils.container\
    import Container

from gen_stix.src.gen_stix.usecase.\
    .attack_pattern_crudl.attack_pattern_crudl_inputport_builder\
    import InputPortBuilder


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/features/gen_stix/sdos/attack_pattern/attack_pattern_crudl.feature",
          "Performing CRUDL operations on a STIX 2.1 AttackPattern.")
def test_attack_pattern_crudl():
    pass


@given(parsers.parse("An AttackPattern is created with {type_}, {name}, and {description}."), target_fixture="context")
def given_attack_pattern_crudl(type_, name, description):
    input_contract = InputPortBuilder()\
        .create()\
        .with_type_(type_)\
        .with_name(name)\
        .with_description(description)\
        .build()

    return {
        "type_": type_,
        "name": name,
        "description": description,
        "input_contract": input_contract
    }


@when(parsers.parse("The AttackPattern is created, updated with {new_description}, and deleted."))
def when_attack_pattern_crudl(context, new_description):
    usecase = Container.get_usecase_repo("", STORAGE_ENGINE)
    output_contract = usecase.execute(context["input_contract"])
    context["output_contract"] = output_contract


@then(parsers.parse("An AttackPattern should exist with {new_description}, {name}, and {type_}, and one AttackPattern should be deleted."))
def then_attack_pattern_crudl(context, new_description, name, type_):
    assert context["output_contract"]\
        .new_description == new_description
    assert context["output_contract"]\
        .name == name
    assert context["output_contract"]\
        .type_ == type_
```

As you can see, a lot of boilerplate has been written for us, so let's complete some of the missing information.

First, in the Gherkin file, we need to provide data to test.
To do this, adjust the example tables like this:

```gherkin
Feature: CRUDL for the STIX 2.1 object AttackPattern.

    Scenario Outline: Performing CRUDL operations on a STIX 2.1 AttackPattern.
        Given An AttackPattern is created with <type_>, <name>, and <description>.
        When The AttackPattern is created, updated with <new_description>, and deleted.
        Then An AttackPattern should exist with <new_description>, <name>, and <type_>, and one AttackPattern should be deleted.

        Examples:
            | type_          | name           | description         | new_description               |
            | attack-pattern | AttackPattern1 | AttackPattern1_desc | AttackPattern1_desc           |
            | attack-pattern | AttackPattern2 | AttackPattern2_desc | AttackPattern2DescUpdated     |
            | attack-pattern | AttackPattern3 | AttackPattern3_desc | AttackPattern3DescToBeDeleted |
```

CRUDL features are not really atomic. I find it quite annoying to test all six features separately, as they essentially do the same thing. So, I have come up with a workflow where I try to handle them all in one go.

Okay, now let's add some code in the associated test.

```python
import os

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers

from gen_stix.tests.factory\
    import Factory

from gen_stix.src.utils.container\
    import Container

from gen_stix.src.gen_stix.usecase.\
    sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder\
    import CreateAttackPatternInputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    sdos.attack_pattern.update_attack_pattern.update_attack_pattern_inputport_builder\
    import UpdateAttackPatternInputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_inputport_builder\
    import DeleteAttackPatternInputPortBuilder


STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.order()
@scenario(f"{__fullpath.split('/GenSTIX/')[0]}"
          "/GenSTIX/gen_stix"
          "/features/gen_stix/sdos/attack_pattern/attack_pattern_crudl.feature",
          "Performing CRUDL operations on a STIX 2.1 AttackPattern.")
def test_attack_pattern_crudl():
    pass


@given(parsers.parse("An AttackPattern is created with {type_}, {name}, and {description}."), target_fixture="context")
def given_attack_pattern_crudl(type_, name, description):
    input_contract = CreateAttackPatternInputPortBuilder()\
        .create()\
        .with_type_(type_)\
        .with_name(name)\
        .with_description(description)\
        .build()

    return {
        "type_": type_,
        "name": name,
        "description": description,
        "input_contract": input_contract
    }


@when(parsers.parse("The AttackPattern is created, updated with {new_description}, and deleted."))
def when_attack_pattern_crudl(context, new_description):
    usecase = Container.get_usecase_repo("CreateAttackPattern", STORAGE_ENGINE)
    create_contract = usecase.execute(context["input_contract"])

    if "Updated" in new_description:
        input_contract = UpdateAttackPatternInputPortBuilder()\
            .create()\
            .with_type_(context["type_"])\
            .with_name(context["name"])\
            .with_description(new_description)\
            .build()
        usecase = Container.get_usecase_repo("UpdateAttackPattern", STORAGE_ENGINE)
        update_contract = usecase.execute(input_contract)
        output_contract = update_contract
    elif "Deleted" in new_description:
        input_contract = DeleteAttackPatternInputPortBuilder()\
            .create()\
            .with_type_(context["type_"])\
            .with_name(context["name"])\
            .build()
        usecase = Container.get_usecase_repo("DeleteAttackPattern", STORAGE_ENGINE)
        delete_contract = usecase.execute(input_contract)
        output_contract = delete_contract
    else:
        output_contract = create_contract

    context["output_contract"] = output_contract


@then(parsers.parse("An AttackPattern should exist with {new_description}, {name}, and {type_}, and one AttackPattern should be deleted."))
def then_attack_pattern_crudl(context, new_description, name, type_):
    if "Deleted" not in new_description:
        assert context["output_contract"]\
            .type_ == type_
        assert context["output_contract"]\
            .name == name
        assert context["output_contract"]\
            .description == new_description
    else:
        assert context["output_contract"]\
            .deleted == True
```

I recommend creating all the constraints associated with the feature. It's easier to handle them as a bundle if they aren't too complex. I will only demonstrate one constraint in this README and not all of them. Please refer to the source code if you want to see the others.

#### First constraint: attack_pattern_stix21_required_name

```bash
$ BoilerplateGenerator create-constraint
let's create a new constraint
? Select one project in all of that: GenSTIX
? What's the name of the constraint ? AttackPatternStix21RequiredName
? What types of constraint this will be? core
? What's the constraint domain? sdos/attack_pattern
? Can you describe the constraint? To create a valid STIX 2.1 AttackPattern, the name is a required field.
? Can you describe the scenario? Creating an AttackPattern without a name.
? Can you describe the 'Given' of that scenario? An AttackPattern is created without any name.
? Can you describe the 'When' of that scenario? The AttackPattern is created.
? Can you describe the 'Then' of that scenario? A ValueError should be raised, stating the requirements for the name field.

? Are you sure of the above inputs? Yes
The constraint AttackPatternStix21RequiredName has been created.
```

Let's generate it the same way we did for the feature:

```bash
$ BoilerplateGenerator generate-constraint
let's generate a constraint
? Select one project in all of that: GenSTIX
? Select one constraint in all of that: AttackPatternStix21RequiredName
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/constraints/gen_stix/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_required_name.constraint
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_required_name.py
```

In this particular case, I don't need to make any changes in the constraint file, so let's write the test:

```python
import os

from pytest import mark
from pytest_bdd\
    import scenario, given, when, then, parsers


from gen_stix.tests.factory\
    import Factory

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
          "/constraints/gen_stix/sdos/attack_pattern/attack_pattern_stix21_required_name.constraint",
          "Creating an AttackPattern without a name.")
def test_attack_pattern_stix21_required_name():
    pass


@given(parsers.parse("An AttackPattern is created without any name."), target_fixture="context")
def given_attack_pattern_stix21_required_name():
    input_contract = CreateAttackPatternInputPortBuilder()\
        .create()

    return {
        "input_contract": input_contract
    }



@when(parsers.parse("The AttackPattern is created."))
def when_attack_pattern_stix21_required_name(context):
    try:
        context["input_contract"].build()
    except ValueError as ve:
        context["error"] = ve


@then(parsers.parse("A ValueError should be raised, stating the requirements for the name field."))
def then_attack_pattern_stix21_required_name(context):
    assert type(context["error"]) == ValueError
    assert str(context["error"]) == "`name` is a required field for AttackPattern"
```

let's do a little flake8 on top of that, we can exclude E501, since 80char is not really a thing anymore.

Next, we repeat the same process for all the other involved constraints:
- attack_pattern_stix21_required_type
- attack_pattern_stix2.1_constraint_type
- attack_pattern_stix2.1_constraint_name
- attack_pattern_check_unicity_by_type_name
- attack_pattern_stix21_optional_fields
- attack_pattern_stix2.1_constraint_description
- attack_pattern_stix2.1_constraint_aliases

Special focus on two constraints:
- attack_pattern_stix2.1_constraint_kill_chain_phases
- attack_pattern_stix2.1_constraint_external_references

These are particularly interesting because they validate two new entities we didn't identify earlier: kill-chain-phase and external-references. They also have their own constraints.

To fulfill the constraint for AttackPattern, we need to create kill-chain-phase and external-references first. That’s what I did in my code. So for the purpose of this documentation, just know that I created these entities before proceeding to the next step with AttackPattern.

You can check the related constraints and features; they are quite simple and follow the same workflow described in this documentation.
