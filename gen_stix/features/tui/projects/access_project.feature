Feature: Access a project.

    Scenario Outline: Access a projects by pressing 'enter' on it.
        Given I'm in the tui app, with a project <project_name> created.
        When I press 'enter' on that project.
        Then I should see a list of Category STIX (sdos,scos,cdts,..) in that project.

        Examples:
            | |
            | |