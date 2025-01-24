Feature: When pressing 'r' on 'Kill Chain Phase' i have a form allowing us to search an object.

    Scenario Outline: Will search and access an existing Kill Chain Phase Object.
        Given I'm in the app in tui mode with a valid <projects_path>, <project_name> and i have a valid Kill Chain Phase created with <kill_chain_name>, <phase_name>.
        When I press 'r' on 'Kill Chain Phase' in the navtree, i have a search form, when i fulfill it and pres 'enter'.
        Then I should see the corresponding Kill Chain Phase object and the json output.

        Examples:
            | |
            | |