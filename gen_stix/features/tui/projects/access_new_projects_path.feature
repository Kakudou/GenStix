Feature: Accessing and creating a new projects path.

    Scenario Outline: Accessing and create a new projects path.
        Given I start the app in tui mode.
        When I provide a new <projects_path>.
        Then I should access the HomeScreen for that <projects_path>.

        Examples:
            | |
            | |