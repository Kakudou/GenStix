# GenSTIX Contributing Guide

## TL;DR

###  Workflow for a New Feature

####Plan and Define Behavior

Identify the feature's scope and purpose.
Write Gherkin feature files using BDD syntax (Given, When, Then).
Add constraints to define the rules for validation and business logic.

#### Write Unit Tests First (TDD)

Create pytest test cases to cover all edge cases and expected behaviors, including constraints.
Run tests to ensure they fail before writing the feature code.

#### Develop the Core Logic

##### Entity Creation

Implement or update the relevant domain entity to represent the feature concept (e.g., AttackPattern).

##### Use Case Implementation

Write the use case logic that orchestrates the feature's behavior and enforces constraints.

##### Validate Input

Add an input validator to ensure inputs align with the expected schema and rules.

#### Integrate Behavior Tests (BDD)

Run Gherkin scenarios as integration tests to ensure the feature works as expected in a complete flow.

#### Refactor and Test

Refactor code for clarity, modularity, and compliance with Clean Architecture principles.
Ensure all tests pass (pytest).

#### Document the Feature

Update or create documentation for the feature (e.g., CLI usage, API calls, examples).

#### Submit for Review

Rebase your branch with the latest main.
Check for consistency, correctness, and adherence to project standards.
Submit a pull request with a clear description of the changes and test coverage.

#### Pull Request Process

Checklist Before Opening a PR:

  - [ ] Ensure your feature branch is rebased with the latest main.
  - [ ] Double-check that all unit tests and integration tests pass (pytest).
  - [ ] Verify documentation is updated and correctly describes the new feature.
  - [ ] Use meaningful commit messages with gitmoji, and squash unnecessary commits.

#### Submit the Pull Request

Include a clear description of the changes.
Provide a summary of the feature, behavior, and purpose.
Attach test results or relevant screenshots if needed.
Add reviewers and labels (e.g., feature, bugfix).

#### Respond to Feedback

Address code review comments promptly.
Make iterative changes as requested and rebase if necessary.

### General Guidelines

Always follow Clean Architecture principles and adhere to TDD/BDD workflows.
Write clean, modular, and testable code.
Respect feedback and iterate quickly on reviews.

### Environment Setup

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

### Branching Strategy
Create a Feature Branch:

```bash
git checkout -b feature/<your-feature-name>
```

### Commit and Push

Use clear and atomic commits, bonuses for gitmoji usage.

```bash
git commit -m ":sparkles: Add feature XYZ"
git push origin feature/<your-feature-name>
```

### Code Standards

Follow PEP 8 for Python coding style.
Write clear and concise docstrings for every module, class, and function.
Use type hints to maintain code readability and consistency.

### Documentation Requirements

Include a description of the feature, its purpose, and examples of usage.
Document any new CLI commands, API endpoints, or configuration options.
Ensure documentation is easy to follow for new contributors or users.

Treat documentation as a core part of the feature and separate commit updates from your code.

### Examples and Tutorials

Provide example workflows, Gherkin files, or usage instructions in README or other docs.

