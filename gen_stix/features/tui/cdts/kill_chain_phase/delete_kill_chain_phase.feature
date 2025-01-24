Feature: Delete an existing Kill Chain Phase.

    Scenario Outline: When pressing 'd' on an existing Kill chain phase object, we should nbe able to delete it.
        Given I'm in the app in tui mode, with a valid <projects_path>, <project_name> and i have a valid Kill chain Phase created with <kill_chain_name> and <phase_name>.
        When I press 'd' on the object, i should get a form to validate the deletion, when pressing 'enter' i validate it.
        Then The Kill Chain Phase object should've been deleted.

        Examples:
            | |
            | |