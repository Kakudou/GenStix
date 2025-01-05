"""This module handle the data access in memory"""

from hashlib import sha256
from typing import List

from gen_stix.src.utils.singleton import Singleton
from gen_stix.src.app.dto.cdts.external_reference.external_reference_dto import (
    ExternalReferenceDTO,
)
from gen_stix.src.gen_stix.gateway.cdts.external_reference.external_reference_gateway import (
    ExternalReferenceGateway,
)
from gen_stix.src.gen_stix.entity.cdts.external_reference.external_reference import (
    ExternalReference,
)
from gen_stix.src.app.repository.inmemory.inmemory_persist import (
    InMemoryPersist,
)


@Singleton
class ExternalReferenceINMEMORYRepository(ExternalReferenceGateway):
    """ "This class implement the ExternalReferenceGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the ExternalReference inmemory dict
    exist_by_identifier:
        will check if an ExternalReference with this identifier exist
    update_by_identifier:
        will 'update' the ExternalReference inmemory dict
    find_all:
        will search all ExternalReference
    find_by_identifier:
        will search an ExternalReference by his identifier
    destroy_by_identifier:
        will delete an ExternalReference by his identifier
    _convert_to_dto:
        convert core ExternalReference to ExternalReferenceDTO
    _convert_to_entity:
        convert ExternalReferenceDTO to core ExternalReference
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.external_references = {}

    def _generate_id(self, identifier) -> str:
        """This function will generate an ID for the entity
        base on his identifier

        Returns:
        --------
        str
            the identifier hash

        """

        id = sha256(str(identifier).encode()).hexdigest()

        return id

    def save(self, external_reference: ExternalReference) -> bool:
        """This function will save ExternalReference as ExternalReferenceDTO

        Parameters:
        -----------
        external_reference: ExternalReference
            The ExternalReference that we will be saved and convert as ExternalReferenceDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        external_reference_dto = self._convert_to_dto(external_reference)
        self.__persists.external_references[external_reference_dto.id] = (
            external_reference_dto
        )

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check ExternalReference existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the ExternalReference to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.external_references[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(
        self, identifier: str, external_reference: ExternalReference
    ) -> bool:
        """This function will update ExternalReference

        Parameters:
        -----------
        identifier: str
            the identifier for the ExternalReference to update
        external_reference: ExternalReference
            The ExternalReference that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        external_reference_dto = self._convert_to_dto(external_reference)
        self.__persists.external_references[external_reference_dto.id] = (
            external_reference_dto
        )

        updated = True

        return updated

    def find_all(self) -> List[ExternalReference]:
        """This function will find all ExternalReference

        Parameters:
        -----------

        Returns:
        --------
        List[ExternalReference]:
            all ExternalReference

        """

        external_references = []
        for external_reference_id in self.__persists.external_references:
            external_reference_dto = self.__persists.external_references[
                external_reference_id
            ]
            external_reference = self._convert_to_entity(
                external_reference_dto
            )
            external_references.append(external_reference)

        return external_references

    def find_by_identifier(self, identifier: str) -> ExternalReference:
        """This function will find ExternalReference by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for ExternalReference to find

        Returns:
        --------
        ExternalReference:
            The ExternalReference

        """

        external_reference = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            external_reference_dto = self.__persists.external_references[
                hash_id
            ]
        except KeyError:
            external_reference_dto = None

        if external_reference_dto is not None:
            external_reference = self._convert_to_entity(
                external_reference_dto
            )

        return external_reference

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete ExternalReference

        Parameters:
        -----------
        identifier: str
            The identifier for the ExternalReference to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        external_reference_id = self._generate_id(identifier)
        del self.__persists.external_references[external_reference_id]

        deleted = True

        return deleted

    def _convert_to_dto(
        self, external_reference: ExternalReference
    ) -> ExternalReferenceDTO:
        """This function will convert ExternalReference to a ExternalReferenceDTO

        Parameters:
        -----------
        external_reference: ExternalReference
            Entity ExternalReference as seen by the core

        Returns:
        --------
        ExternalReferenceDTO
            the ExternalReferenceDTO ready to be persist

        """

        identifier = (
            external_reference.source_name,
            external_reference.external_id,
        )

        external_reference_dto = ExternalReferenceDTO()
        external_reference_dto.id = self._generate_id(identifier)
        external_reference_dto.source_name = external_reference.source_name
        external_reference_dto.description = external_reference.description
        external_reference_dto.url = external_reference.url
        external_reference_dto.hashes = external_reference.hashes
        external_reference_dto.external_id = external_reference.external_id

        return external_reference_dto

    def _convert_to_entity(
        self, external_reference_dto: ExternalReferenceDTO
    ) -> ExternalReference:
        """This function will convert a ExternalReferenceDTO to ExternalReference

        Parameters:
        -----------
        ExternalReferenceDTO
            the ExternalReferenceDTO ready to be persist

        Returns:
        --------
        external_reference: ExternalReference
            Entity ExternalReference as seen by the core

        """

        external_reference = ExternalReference()
        external_reference.source_name = external_reference_dto.source_name
        external_reference.description = external_reference_dto.description
        external_reference.url = external_reference_dto.url
        external_reference.hashes = external_reference_dto.hashes
        external_reference.external_id = external_reference_dto.external_id

        return external_reference
