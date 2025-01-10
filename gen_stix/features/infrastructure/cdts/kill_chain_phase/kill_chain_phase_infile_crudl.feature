Feature: CRUDL operations for the STIX2.1 Kill Chain Phase Object, with persistence in a file per object.

    Scenario Outline: Performing CRUDL operations on a STIX2.1 Kill Chain Phase.
        Given A Kill Chain Phase is created with <kill_chain_name> and <phase_name>.
        When The Kill Chain Phase is create, read, update, list and deleted.
        Then The Kill Chain Phase should be retrieve from the file if exists.

        Examples:
            | kill_chain_name                 | phase_name           |
            | create-infile-custom-kill-chain | custom-value         |
            | update-infile-custom-kill-chain | custom-value-updated |
            | delete-infile-custom-kill-chain | custom-value-deleted |
