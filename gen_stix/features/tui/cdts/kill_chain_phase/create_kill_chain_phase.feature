Feature: Create a Kill Chain Phase

    Scenario Outline: Create a Kill Chain Phase STIX2.1 Object.
        Given I'm in the tui app, in a valid <projects_path> and <project_name>. when i press 'c' on 'Kill Chain Phase' in the 'CDTs' list.
        When I have a form i should fill with a valid <kill_chain_name> and <phase_name> then press 'enter'.
        Then I should have the Kill Chain Phase object created, and i should see the json output.

        Examples:
            | |
            | |