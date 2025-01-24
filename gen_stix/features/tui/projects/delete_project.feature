Feature: Delete a project and all contained objects.

    Scenario Outline: When pressing 'd' on a project, i should be able to delete it.
        Given I'm on the app in tui node, with a valid <projects_path> and a <project_name> created.
        When i press 'd' on the <project_name> after completing and validating the deletion form.
        Then The project should no longer exists.

        Examples:
            | |
            | |