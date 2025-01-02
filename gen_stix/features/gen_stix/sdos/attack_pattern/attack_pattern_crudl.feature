Feature: CRUDL for the STIX 2.1 object AttackPattern.

    Scenario Outline: Performing CRUDL operations on a STIX 2.1 AttackPattern.
        Given An AttackPattern is created with <type_>, <name>, and <description>.
        When The AttackPattern is created, updated with <new_description>, and deleted.
        Then An AttackPattern should exist with <new_description>, <name>, and <type_>, and one AttackPattern should be deleted.

        Examples:
            | type_          | name           | description         | new_description               |
            | attack-pattern | CreateAttackPattern1 | AttackPattern1_desc | AttackPattern1_desc           |
            | attack-pattern | CreateAttackPattern2 | AttackPattern2_desc | AttackPattern2DescUpdated     |
            | attack-pattern | CreateAttackPattern3 | AttackPattern3_desc | AttackPattern3DescToBeDeleted |
