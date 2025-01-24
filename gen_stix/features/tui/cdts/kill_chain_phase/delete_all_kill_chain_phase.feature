Feature: Delete all Kill Chain Phase

    Scenario Outline: When pressing 'd' on 'Kill Chain Phase', we should be able to delete them all at once.
        Given I'm in the app in tui mode, with a valid <projects_path>, <project_name>, and i have few valid Kill Chain Phase object created with <kill_chain_name>, <phase_name>.
        When I press 'd' on the 'Kill Chain Phase' i should get a validation form to delete them all at once.
        Then Once validate, they should all be deleted.

        Examples:
            | |
            | |