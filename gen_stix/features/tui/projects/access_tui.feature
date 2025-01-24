Feature: Accessing the TUI of the App.

    Scenario Outline: Accessing the TUI of the App should show us the main screen.
        Given I launch the app using the --tui arguments.
        When The app starts.
        Then i should got the Starting Screen.

        Examples:
            | |
            | |