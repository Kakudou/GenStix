"""This module handle the data access in file"""

from os import makedirs, path, listdir, remove
from hashlib import sha256
from typing import List
from json import dumps as json_dumps

from gen_stix.src.gen_stix.entity.enums.external_reference_capec import (
    ExternalReferenceCapec,
)
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
from gen_stix.src.app.repository.infile.infile_persist import (
    InFilePersist,
)


@Singleton
class ExternalReferenceINFILERepository(ExternalReferenceGateway):
    """ "This class implement the ExternalReferenceGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the ExternalReference infile dict
    exist_by_identifier:
        will check if an ExternalReference with this identifier exist
    update_by_identifier:
        will 'update' the ExternalReference infile dict
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
        """Init InFilePersist who will be used for infile storage"""

        self.__persists = InFilePersist()
        self.__files_path = (
            f"{self.__persists.save_path}/cdts/external_reference"
        )

    def _update_files_path(self):
        self.__persists = InFilePersist()
        self.__files_path = (
            f"{self.__persists.save_path}/cdts/external_reference"
        )

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
        self._update_files_path()

        saved = False

        external_reference_dto = self._convert_to_dto(external_reference)
        stix21 = external_reference_dto.to_stix21()
        external_reference.stix_representation = stix21

        file_dest = f"{self.__files_path}/{external_reference_dto.id}.json"

        makedirs(self.__files_path, exist_ok=True)

        with open(file_dest, "w") as file:
            file.write(json_dumps(stix21))

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

        self._update_files_path()

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        file_dest = f"{self.__files_path}/{hash_id}.json"
        exist = path.isfile(file_dest)

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

        # ExternalReference only got identifier att, so we can't update it

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all ExternalReference

        Parameters:
        -----------

        Returns:
        --------
        List[ExternalReference]:
            all ExternalReference

        """

        self._update_files_path()

        external_references = []
        if path.isdir(self.__files_path):
            for file in listdir(self.__files_path):
                if path.isfile(f"{self.__files_path}/{file}"):
                    with open(f"{self.__files_path}/{file}", "r") as file:
                        external_reference_dto = ExternalReferenceDTO()
                        external_reference_dto.from_stix21(file.read())
                        external_reference = self._convert_to_entity(
                            external_reference_dto
                        )
                        if external_reference.source_name.lower() == "capec":
                            external_references.append(
                                f"{external_reference.source_name} - {ExternalReferenceCapec.from_id(external_reference.external_id.split("CAPEC-")[1]).name}"
                            )
                        else:
                            external_references.append(
                                f"{external_reference.source_name} - {external_reference.external_id}"
                            )

        return external_references

    def find_by_identifier(self, identifier: str) -> ExternalReference | None:
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

        self._update_files_path()

        external_reference = None

        if self.exist_by_identifier(identifier):
            with open(
                f"{self.__files_path}/{self._generate_id(identifier)}.json",
                "r",
            ) as file:
                external_reference_dto = ExternalReferenceDTO()
                external_reference_dto.from_stix21(file.read())
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

        self._update_files_path()

        deleted = False

        if self.exist_by_identifier(identifier):
            path_to_delete = (
                f"{self.__files_path}/{self._generate_id(identifier)}.json"
            )
            remove(path_to_delete)
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
        external_reference_dto.external_id = external_reference.external_id
        external_reference_dto.description = external_reference.description
        external_reference_dto.url = external_reference.url
        external_reference_dto.hashes = external_reference.hashes

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
        external_reference.external_id = external_reference_dto.external_id
        external_reference.description = external_reference_dto.description
        external_reference.url = external_reference_dto.url
        external_reference.hashes = external_reference_dto.hashes
        external_reference.stix_representation = (
            external_reference_dto.to_stix21()
        )

        return external_reference
