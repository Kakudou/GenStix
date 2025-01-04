Feature: CRUDL for the STIX 2.1 object ExternalReference.

    Scenario Outline: Performing CRUDL operations on a STIX 2.1 ExternalReference.
        Given An ExternalReference is created with <source_name>, <description>.
        When The ExternalReference is created, updated with <new_description> and deleted.
        Then An ExternalReference should exist with <new_description>, and <source_name>, and one ExternalReference should be deleted.

        Examples:
            | source_name        | description         | new_description      |
            | CreateExternalRef  | Create External Ref | Create External Ref  |
            | UpdateExternalRef  | External Ref        | Updated External Ref |
            | DeletedExternalRef | External Ref        | Deleted External Ref |
