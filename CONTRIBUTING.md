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

<details>
  <summary>test_attack_pattern_crudl.py</summary>

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
</details>


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

<details>
  <summary>test_attack_pattern_crudl.py</summary>

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
</details>


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

<details>
  <summary>test_attack_pattern_stix21_required_name.py</summary>
  
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
</details>


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


#### Create Entity: AttackPattern
Now we can execute our test and confirm that everything is beautifully marked in red (indicating failing tests).
We are now ready to implement the minimum code required to make all these tests pass.

To do this, let's stay organized.

First, we will create the Entity using my framework. It's fairly easy:

```bash
$ BoilerplateGenerator create-entity
let's create a new entity
? Select one project in all of that: GenSTIX
? What's the entity name? AttackPattern
? What's the entity domain? sdos/attack_pattern

? Would you like to add another attribute? Yes
? What's the attribute name? type_
? What's the attribute description? The value of this property **MUST** be attack-pattern.
? What's the attribute type? str
? That attribute should be consider as an identifier? Yes

? Would you like to add another attribute? Yes
? What's the attribute name? external_references
? What's the attribute description? A list of external references which refer to non-STIX information.  This property MAY be used to provide one or more Attack Pattern identifiers, such as a CAPEC ID. When specifying a CAPEC ID, the source_name property of the external reference MUST be set to capec and the external_id property MUST be formatted as CAPEC-[id].
? What's the attribute type? List
? That attribute should be consider as an identifier? No

? Would you like to add another attribute? Yes
? What's the attribute name? name
? What's the attribute description? A name used to identify the Attack Pattern.
? What's the attribute type? str
? That attribute should be consider as an identifier? Yes

? Would you like to add another attribute? Yes
? What's the attribute name? description
? What's the attribute description? A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.
? What's the attribute type? str
? That attribute should be consider as an identifier? No

? Would you like to add another attribute? Yes
? What's the attribute name? aliases
? What's the attribute description? Alternative names used to identify this Attack Pattern.
? What's the attribute type? List[str]
? That attribute should be consider as an identifier? No

? Would you like to add another attribute? Yes
? What's the attribute name? kill_chain_phases
? What's the attribute description? The list of Kill Chain Phases for which this Attack Pattern is used.
? What's the attribute type? List
? That attribute should be consider as an identifier? No

? Would you like to add another attribute? No

? Are you sure of the above inputs? Yes
The entity AttackPattern has been created.
```

Next, we generate all the associated code:

```bash
$ BoilerplateGenerator generate-entity
let's generate an entity
? Select one project in all of that: GenSTIX
? Select one entity in all of that: AttackPattern
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/dto/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/repository/inmemory/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/entity/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/gateway/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/cli/entity_view/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/api/entity_view/sdos/attack_pattern/
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/tui/entity_view/sdos/attack_pattern/

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/dto/sdos/attack_pattern/attack_pattern_dto.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/repository/inmemory/sdos/attack_pattern/attack_pattern_inmemory_repository.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/entity/sdos/attack_pattern/attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/gateway/sdos/attack_pattern/attack_pattern_gateway.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/cli/entity_view/sdos/attack_pattern/attack_pattern_view.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/api/entity_view/sdos/attack_pattern/attack_pattern_view.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/tui/entity_view/sdos/attack_pattern/attack_pattern_view.py
```

#### Create CRUDL UseCases

Finally, we create and generate the CRUDL (Create, Read, Update, Delete, List) functionality for that entity:

```bash
$ BoilerplateGenerator create-crudl
let's create a full CRUDL
? Select one project in all of that: GenSTIX
? Select one entity in all of that: AttackPattern
-----

? Are you sure you want to generate CRUDL for AttackPattern? Yes

The usecase CreateAttackPattern has been created.
The usecase ReadAttackPattern has been created.
The usecase UpdateAttackPattern has been created.
The usecase DeleteAttackPattern has been created.
The usecase ListAttackPattern has been created.
```

```bash
$ BoilerplateGenerator generate-crudl
let's generate the CRUDL
? Select one project in all of that: GenSTIX
? Select one entity in all of that: AttackPattern
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/create_attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/create_attack_pattern/create_attack_pattern_adapter.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern/create_attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern/create_attack_pattern_inputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern/create_attack_pattern_inputport_builder.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern/create_attack_pattern_outputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/create_attack_pattern/create_attack_pattern_outputport_builder.py
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/read_attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/read_attack_pattern/read_attack_pattern_adapter.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern/read_attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern/read_attack_pattern_inputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern/read_attack_pattern_inputport_builder.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern/read_attack_pattern_outputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/read_attack_pattern/read_attack_pattern_outputport_builder.py
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/update_attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/update_attack_pattern/update_attack_pattern_adapter.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern/update_attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern/update_attack_pattern_inputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern/update_attack_pattern_inputport_builder.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern/update_attack_pattern_outputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/update_attack_pattern/update_attack_pattern_outputport_builder.py
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/delete_attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern_adapter.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern_inputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern_inputport_builder.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern_outputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/delete_attack_pattern/delete_attack_pattern_outputport_builder.py
-----

The following folders have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/list_attack_pattern
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern

The following files have been created:
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/app/adapter/sdos/attack_pattern/list_attack_pattern/list_attack_pattern_adapter.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern/list_attack_pattern.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern/list_attack_pattern_inputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern/list_attack_pattern_inputport_builder.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern/list_attack_pattern_outputport.py
/home/kakudou/construct/python/WiP/GenSTIX/gen_stix/src/gen_stix/usecase/sdos/attack_pattern/list_attack_pattern/list_attack_pattern_outputport_builder.py
```

As you can see, using the framework allows me to maintain peace of mind. Although I love Clean Architecture, it often requires creating a lot of classes. Automating that part is a lifesaver.
For fun, let's run the tests at this point.


```bash
$ pytest
============================================================================================ test session starts =============================================================================================
platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/kakudou/construct/python/WiP/GenSTIX
configfile: pyproject.toml
plugins: order-1.3.0, bdd-8.1.0
collected 44 items

gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_check_unicity_by_type_name.py FF                                                                                           [ 10%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_aliases.py FFF                                                                                           [ 26%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_description.py FF                                                                                        [ 36%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_external_references.py F                                                                                 [ 42%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_kill_chain_phases.py F                                                                                   [ 47%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_name.py F                                                                                                [ 52%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_type.py F                                                                                                [ 57%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_optional_fields.py FFF                                                                                              [ 73%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_required_name.py F                                                                                                  [ 78%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_required_type.py F                                                                                                  [ 84%]
gen_stix/tests/features/gen_stix/sdos/attack_pattern/test_attack_pattern_crudl.py FFF                                                                                                                  [100%]

[...] 

FAILED gen_stix/tests/features/gen_stix/sdos/attack_pattern/test_attack_pattern_crudl.py::test_attack_pattern_crudl[attack-pattern-AttackPattern3-AttackPattern3_desc-AttackPattern3DescToBeDeleted] - NotImplementedError
============================================================================================= 44 failed in 0.30s =============================================================================================
```

I haven't copied the full output since it's repetitive, but essentially, we encounter a NotImplementedError. This occurs because of our input_builder, which requires implementing the checks we want to perform on the input.
Let's take a look at create_attack_pattern_inputport_builder.py:

<details>
  <summary>create_attack_pattern_inputport_builder.py</summary>

```python
"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from gen_stix.src.gen_stix.usecase.\
    sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport\
    import CreateAttackPatternInputPort


@dataclass
class CreateAttackPatternInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: CreateAttackPatternInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_type_: str
        fill the type_ in the contract
    with_external_references: List
        fill the external_references in the contract
    with_name: str
        fill the name in the contract
    with_description: str
        fill the description in the contract
    with_aliases: List[str]
        fill the aliases in the contract
    with_kill_chain_phases: List
        fill the kill_chain_phases in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        CreateAttackPatternInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = CreateAttackPatternInputPort()
        return self

    def with_type_(self, type_: str):
        """ This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_type_(type_)
        self.__input.type_ = type_
        return self

    def _validate_type_(self, type_: str):
        """ This function check the  validity of type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def with_external_references(self, external_references: List):
        """ This function fill the external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_external_references(external_references)
        self.__input.external_references = external_references
        return self

    def _validate_external_references(self, external_references: List):
        """ This function check the  validity of external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_name(name)
        self.__input.name = name
        return self

    def _validate_name(self, name: str):
        """ This function check the  validity of name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def with_description(self, description: str):
        """ This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_description(description)
        self.__input.description = description
        return self

    def _validate_description(self, description: str):
        """ This function check the  validity of description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def with_aliases(self, aliases: List[str]):
        """ This function fill the aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_aliases(aliases)
        self.__input.aliases = aliases
        return self

    def _validate_aliases(self, aliases: List[str]):
        """ This function check the  validity of aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def with_kill_chain_phases(self, kill_chain_phases: List):
        """ This function fill the kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_kill_chain_phases(kill_chain_phases)
        self.__input.kill_chain_phases = kill_chain_phases
        return self

    def _validate_kill_chain_phases(self, kill_chain_phases: List):
        """ This function check the  validity of kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------

        """
        raise NotImplementedError


    def build(self) -> CreateAttackPatternInputPort:
        """ This function return the filled contract

        Returns:
        --------
        CreateAttackPatternInputPort
            the contract filled

        """

        self._validate_type_(self.__input.type_)
        self._validate_external_references(self.__input.external_references)
        self._validate_name(self.__input.name)
        self._validate_description(self.__input.description)
        self._validate_aliases(self.__input.aliases)
        self._validate_kill_chain_phases(self.__input.kill_chain_phases)

        return self.__input
```
</details>


As you can see, the builder creates several setter functions like with_xxx, which call _validate_xxx.
Currently, _validate raises a NotImplementedError. We need to implement all the checks we outlined in our constraints within these methods.
We'll need to do this for each inputport_builder in each CRUDL use case. For this guide, I'll only focus on the "create" use case.

<details>
  <summary>create_attack_pattern_inputport_builder.py</summary>

```python
"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List, Dict
from gen_stix.src.gen_stix.usecase.\
    sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport\
    import CreateAttackPatternInputPort


@dataclass
class CreateAttackPatternInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: CreateAttackPatternInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_type_: str
        fill the type_ in the contract
    with_external_references: List
        fill the external_references in the contract
    with_name: str
        fill the name in the contract
    with_description: str
        fill the description in the contract
    with_aliases: List[str]
        fill the aliases in the contract
    with_kill_chain_phases: List
        fill the kill_chain_phases in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        CreateAttackPatternInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = CreateAttackPatternInputPort()
        return self

    def with_type_(self, type_: str):
        """ This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_type_(type_)
        self.__input.type_ = type_
        return self

    def _validate_type_(self, type_: str):
        """ This function check the  validity of type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------

        """

        if type_ is None or type == "":
            raise ValueError("`type` is a required field for AttackPattern")
        elif type_ != "attack-pattern":
            raise ValueError("`type` must be `attack-pattern`.")

    def with_external_references(self, external_references: List):
        """ This function fill the external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_external_references(external_references)
        self.__input.external_references = external_references
        return self

    def _validate_external_references(self, external_references: List):
        """ This function check the  validity of external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------

        """

        if external_references is not None:
            if not isinstance(external_references, List):
                raise ValueError("`external_references` must be a List[external-reference].")
            else:
                for external_ref in external_references:
                    if not isinstance(external_ref, Dict):
                        raise ValueError("`external_references` must be a List[external-reference].")
                    elif external_ref["source_name"] is None:
                        raise ValueError("`external_references` must be a List[external-reference].")
                    elif external_ref["source_name"] == "capec" and  external_ref["external_id"] is None:
                        raise ValueError("`external_references` must be a List[external-reference].")
                    elif external_ref["source_name"] == "capec" and not external_ref["external_id"].startswith("CAPEC-"):
                        raise ValueError("`external_references` must be a List[external-reference].")
                    elif external_ref["source_name"] == "":
                        raise ValueError("`external_references` must be a List[external-reference].")


    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_name(name)
        self.__input.name = name
        return self

    def _validate_name(self, name: str):
        """ This function check the  validity of name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------

        """

        if name is None or name == "":
            raise ValueError("`name` is a required field for AttackPattern")
        elif type(name) is not str:
            raise ValueError("`name` must be a str.")



    def with_description(self, description: str):
        """ This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_description(description)
        self.__input.description = description
        return self

    def _validate_description(self, description: str):
        """ This function check the  validity of description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------

        """

        if description is not None:
            if type(description) is not str:
                raise ValueError("`description` must be a str.")


    def with_aliases(self, aliases: List[str]):
        """ This function fill the aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_aliases(aliases)
        self.__input.aliases = aliases
        return self

    def _validate_aliases(self, aliases: List[str]):
        """ This function check the  validity of aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------

        """

        if aliases is not None:
            if not isinstance(aliases, List):
                raise ValueError("`aliases` must be a List[str].")
            elif not all(isinstance(alias, str) for alias in aliases):
                raise ValueError("`aliases` must be a List[str].")


    def with_kill_chain_phases(self, kill_chain_phases: List):
        """ This function fill the kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_kill_chain_phases(kill_chain_phases)
        self.__input.kill_chain_phases = kill_chain_phases
        return self

    def _validate_kill_chain_phases(self, kill_chain_phases: List):
        """ This function check the  validity of kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------

        """

        if kill_chain_phases is not None:
            if not isinstance(kill_chain_phases, List):
                raise ValueError("`kill_chain_phases` must be a List[kill-chain-phase].")
            elif not all(isinstance(kill_chain_phase, Dict) for kill_chain_phase in kill_chain_phases):
                raise ValueError("`kill_chain_phases` must be a List[kill-chain-phase].")

    def build(self) -> CreateAttackPatternInputPort:
        """ This function return the filled contract

        Returns:
        --------
        CreateAttackPatternInputPort
            the contract filled

        """

        self._validate_type_(self.__input.type_)
        self._validate_external_references(self.__input.external_references)
        self._validate_name(self.__input.name)
        self._validate_description(self.__input.description)
        self._validate_aliases(self.__input.aliases)
        self._validate_kill_chain_phases(self.__input.kill_chain_phases)

        return self.__input
```
</details>


#### Run the Tests
Okay, now we can run the tests again with pytest:

```bash
$ pytest
============================================================================== test session starts ==============================================================================
platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/kakudou/construct/python/WiP/GenSTIX
configfile: pyproject.toml
plugins: bdd-8.1.0, order-1.3.0
collected 44 items                                                                                                                                                              

gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_capec_id.py .                                                       [  2%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_description.py .                                                    [  4%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_external_id.py .                                                    [  6%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_hashes.py ..                                                        [ 11%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_source_name.py .                                                    [ 13%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_constraint_url.py .                                                            [ 15%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_optional_fields.py ..                                                          [ 20%]
gen_stix/tests/constraints/gen_stix/cdts/external_reference/test_external_reference_stix21_required_source_name.py .                                                      [ 22%]
gen_stix/tests/constraints/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_check_unicity_by_phase_name_kill_chain_name.py ..                                         [ 27%]
gen_stix/tests/constraints/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_stix21_constraint_kill_chain_name.py ..                                                   [ 31%]
gen_stix/tests/constraints/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_stix21_constraint_phase_name.py ..                                                        [ 36%]
gen_stix/tests/constraints/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_stix21_required_kill_chain_name.py ..                                                     [ 40%]
gen_stix/tests/constraints/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_stix21_required_phase_name.py ..                                                          [ 45%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_check_unicity_by_type_name.py .                                                               [ 47%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_aliases.py ...                                                              [ 54%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_description.py ..                                                           [ 59%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_external_references.py .                                                    [ 61%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_kill_chain_phases.py .                                                      [ 63%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_name.py .                                                                   [ 65%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_constraint_type.py .                                                                   [ 68%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_optional_fields.py ...                                                                 [ 75%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_required_name.py .                                                                     [ 77%]
gen_stix/tests/constraints/gen_stix/sdos/attack_pattern/test_attack_pattern_stix21_required_type.py .                                                                     [ 79%]
gen_stix/tests/features/gen_stix/cdts/external_reference/test_external_reference_crudl.py ...                                                                             [ 86%]
gen_stix/tests/features/gen_stix/cdts/kill_chain_phase/test_kill_chain_phase_crudl.py ...                                                                                 [ 93%]
gen_stix/tests/features/gen_stix/sdos/attack_pattern/test_attack_pattern_crudl.py ...                                                                                     [100%]

============================================================================== 44 passed in 0.35s ===============================================================================
```

And everything works as expected!
Our CoreEngine is complete for the AttackPattern entity.

#### Next Steps: Generate STIX 2.1 Objects from the CLI

Let’s keep in mind our end goal: generating AttackPattern objects in STIX 2.1 format from a CLI call.
At this point, we can only create a Python object representation of STIX 2.1 through code.
Our next step is to convert this into a STIX 2.1 object and enable this functionality via a CLI call.

We can do that from various way, but since we are using the Clean Architecture, we will stop working on the CoreEngine and start working on infrastructure.
This means, we will adapt the code in the repository and from the DTO, so that our python object can be serialized/mapped into a STIX2.1 object using the python-stix2 library.
And after that, we will create a CLI command that will use the STORAGE_ENGINE associated with the repository to store the object and then we will be able to retrieve it through the pre-created Adapter.

By default my framework only generates the Storage Engine for the INMEMORY repository, but you can easily adapt it to use a database or a file system.
And that's what we will do, to make that application more usefull, we will implements a file system storage engine, who will sertialize the STIX 2.1 object into a file and retrieve it from the file.
This will allow us to configure the application to use a particular folder, and so create multiple workspaces, each with its own set of STIX 2.1 objects.

Let's start by adapting the DTO and the repository, but before that, we need to define the Test Plan for this new 'infrastructure feature'.
And later on the same for the CLI command.

#### Gherkins for the Infrastructure Features (STIX 2.1 Object Serialization)

We can start by defining the Test Plan for the DTO and the Repository.

```markdown
We want to ensure that the AttackPattern DTO can be serialized into a STIX 2.1 object.
We want to ensure that the AttackPattern DTO can be deserialized from a STIX 2.1 object.
We want to ensure that the AttackPattern Repository can store a STIX 2.1 object.
We want to ensure that the AttackPattern Repository can retrieve a STIX 2.1 object.
```

Next, same as before, let's write the gherkin feature file for the DTO and the Repository.

```gherkin
Feature: AttackPattern DTO Serialization

  Scenario: Serialize the AttackPattern DTO into a STIX 2.1 object
    Given an AttackPattern DTO
    When the DTO is serialized
    Then the DTO is a valid STIX 2.1 object

  Scenario: Deserialize a STIX 2.1 object into an AttackPattern DTO
    Given a STIX 2.1 object
    When the object is deserialized
    Then the object is a valid AttackPattern DTO

Feature: AttackPattern INMEMORY Repository Storage

  Scenario: Store a STIX 2.1 object into the AttackPattern INMEMORY Repository
    Given a STIX 2.1 object
    When the object is stored
    Then the object is stored in the INMEMORY repository

  Scenario: Retrieve a STIX 2.1 object from the AttackPattern INMEMORY Repository
    Given a STIX 2.1 object
    When the object is retrieved
    Then the object is retrieved from the INMEMORY repository

Feature: AttackPattern INFILE Repository Storage

  Scenario: Store a STIX 2.1 object into the AttackPattern INFILE Repository
    Given a STIX 2.1 object
    When the object is stored
    Then the object is stored in the INFILE repository

  Scenario: Retrieve a STIX 2.1 object from the AttackPattern INFILE Repository
    Given a STIX 2.1 object
    When the object is retrieved
    Then the object is retrieved from the INFILE repository
```

Now, let's generate the test files for the DTO and the Repository.
I will not detail the process, as it is the same as before.
You can always check the code in the repository if you need more information.


#### Gherkins for the CLI Command

The same as before, let's write the gherkin feature file for the CLI command.

Those features will be CRUDL from CLI, but with the STIX 2.1 object serialization and storage.

```gherkin
Feature: AttackPattern CLI Command

  Scenario: Create an AttackPattern STIX 2.1 object from the CLI
    Given a CLI command
    When the command is called with the required arguments
    Then the STIX 2.1 object is created and stored in the repository

  Scenario: Read an AttackPattern STIX 2.1 object from the CLI
    Given a CLI command
    When the command is called with the required arguments
    Then the STIX 2.1 object is retrieved from the repository

  Scenario: Update an AttackPattern STIX 2.1 object from the CLI
    Given a CLI command
    When the command is called with the required arguments
    Then the STIX 2.1 object is updated in the repository

  Scenario: Delete an AttackPattern STIX 2.1 object from the CLI
    Given a CLI command
    When the command is called with the required arguments
    Then the STIX 2.1 object is deleted from the repository

  Scenario: List all AttackPattern STIX 2.1 objects from the CLI
    Given a CLI command
    When the command is called with the required arguments
    Then all the STIX 2.1 objects are listed from the repository
```

And we will follow the same logic as before, generate the test files for the CLI command.
Then we will implement the code to make the tests pass.

#### Conclusion

This guide is a step-by-step process to create a CoreEngine for a STIX 2.1 object using Clean Architecture.
We have created the CoreEngine for the AttackPattern entity, and we have defined the next steps to implement the STIX 2.1 object serialization and storage.
We have also defined the Test Plan for the DTO, Repository, and CLI Command, and we have written the Gherkin feature files for each of them.

