Feature: Accessing the Projects path.

    Scenario Outline: Access the provided Projects path.
        Given I start the app in tui mode.
        When I provide an existing <projects_path>.
        Then I should access the HomeScreen for that <projects_path>.

        Examples:
            | |
            | |