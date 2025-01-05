Feature: CRUDL operations for the STIX 2.1 Kill Chain Phase object.

    Scenario Outline: Performing CRUDL operations on a STIX 2.1 Kill Chain Phase.
        Given A Kill Chain Phase is created with <kill_chain_name> and <phase_name>.
        When The Kill Chain Phase is created, updated, and deleted.
        Then A Kill Chain Phase should exist with <kill_chain_name> and <phase_name>, and one Kill Chain Phase should be deleted.

        Examples:
            | kill_chain_name          | phase_name             |
            | create-custom-kill-chain | custom-value           |
            | create-custom-kill-chain | custom-value-updated   |
            | create-custom-kill-chain | custom-value-deleted   |
