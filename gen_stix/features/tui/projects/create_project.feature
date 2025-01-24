Feature: Create a new project.

    Scenario Outline: Create a new project in projects path when pressing 'c'.
        Given I'm in the tui app with a valid <projects_path>, and i press 'c' on the navtree.
        When The form should appear and in put a valid <project_name> and press 'enter'.
        Then The project should be created and should be visible in the navtree.

        Examples:
            | |
            | |