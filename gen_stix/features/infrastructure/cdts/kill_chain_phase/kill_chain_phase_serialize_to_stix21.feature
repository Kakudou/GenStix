Feature: Serialize a Kill Chain Phase into an STIX object.

    Scenario Outline: Serialize an existing Kill Chain Phase Core object into a valid STIX2.1 object and check the json.
        Given I create a Kill Chain Phase with <kill_chain_name> and <phase_name>.
        When I serialize that object into STIX2.1
        Then I should be able to get the <valid_stix21> json for that object.

        Examples:
            | kill_chain_name            | phase_name           | valid_stix21                                                                                                        |
            | serialize-kill-chain | serialize-phase-name | {"kill_chain_name": "serialize-kill-chain", "phase_name": "serialize-phase-name"} |
