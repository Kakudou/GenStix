Feature: When pressing 'r' on an existing kill chain phase object, i should access it.

    Scenario Outline: Access an exisiting kill chain phase object by pressing 'r' to get the json output.
        Given I'm in the app in tui mode with a valid <projects_path>, <project_name> and i have a valid Kill Chain Phase created with <kill_chain_name> and a <phase_name>.
        When I press 'r' on the existing kill chain phase.
        Then I should see it, and the associated json output.

        Examples:
            | |
            | |