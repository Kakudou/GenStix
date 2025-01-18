"""This module handle the data access in file"""

from os import makedirs, path, listdir, remove
from hashlib import sha256
from typing import List
from json import dumps as json_dumps

from gen_stix.src.utils.singleton import Singleton
from gen_stix.src.app.dto.cdts.kill_chain_phase.kill_chain_phase_dto import (
    KillChainPhaseDTO,
)
from gen_stix.src.gen_stix.gateway.cdts.kill_chain_phase.kill_chain_phase_gateway import (
    KillChainPhaseGateway,
)
from gen_stix.src.gen_stix.entity.cdts.kill_chain_phase.kill_chain_phase import (
    KillChainPhase,
)
from gen_stix.src.app.repository.infile.infile_persist import (
    InFilePersist,
)


@Singleton
class KillChainPhaseINFILERepository(KillChainPhaseGateway):
    """ "This class implement the KillChainPhaseGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the KillChainPhase infile dict
    exist_by_identifier:
        will check if an KillChainPhase with this identifier exist
    update_by_identifier:
        will 'update' the KillChainPhase infile dict
    find_all:
        will search all KillChainPhase
    find_by_identifier:
        will search an KillChainPhase by his identifier
    destroy_by_identifier:
        will delete an KillChainPhase by his identifier
    _convert_to_dto:
        convert core KillChainPhase to KillChainPhaseDTO
    _convert_to_entity:
        convert KillChainPhaseDTO to core KillChainPhase
    """

    def __init__(self):
        """Init InFilePersist who will be used for infile storage"""

        self.__persists = InFilePersist()
        self.__files_path = (
            f"{self.__persists.save_path}/cdts/kill_chain_phase"
        )

    def _update_files_path(self):
        self.__persists = InFilePersist()
        self.__files_path = (
            f"{self.__persists.save_path}/cdts/kill_chain_phase"
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

    def save(self, kill_chain_phase: KillChainPhase) -> bool:
        """This function will save KillChainPhase as KillChainPhaseDTO

        Parameters:
        -----------
        kill_chain_phase: KillChainPhase
            The KillChainPhase that we will be saved and convert as KillChainPhaseDTO

        Returns:
        --------
        bool
            True if saved

        """
        self._update_files_path()

        saved = False

        kill_chain_phase_dto = self._convert_to_dto(kill_chain_phase)
        stix21 = kill_chain_phase_dto.to_stix21()
        kill_chain_phase.stix_representation = stix21

        file_dest = f"{self.__files_path}/{kill_chain_phase_dto.id}.json"

        makedirs(self.__files_path, exist_ok=True)

        with open(file_dest, "w") as file:
            file.write(json_dumps(stix21))

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check KillChainPhase existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the KillChainPhase to check

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
        self, identifier: str, kill_chain_phase: KillChainPhase
    ) -> bool:
        """This function will update KillChainPhase

        Parameters:
        -----------
        identifier: str
            the identifier for the KillChainPhase to update
        kill_chain_phase: KillChainPhase
            The KillChainPhase that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        # KillChainPhase only got identifier att, so we can't update it

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all KillChainPhase

        Parameters:
        -----------

        Returns:
        --------
        List[KillChainPhase]:
            all KillChainPhase

        """

        self._update_files_path()

        kill_chain_phases = []
        if path.isdir(self.__files_path):
            for file in listdir(self.__files_path):
                if path.isfile(f"{self.__files_path}/{file}"):
                    with open(f"{self.__files_path}/{file}", "r") as file:
                        kill_chain_phase_dto = KillChainPhaseDTO()
                        kill_chain_phase_dto.from_stix21(file.read())
                        kill_chain_phase = self._convert_to_entity(
                            kill_chain_phase_dto
                        )
                        kill_chain_phases.append(
                            f"{kill_chain_phase.kill_chain_name} - {kill_chain_phase.phase_name}"
                        )

        return kill_chain_phases

    def find_by_identifier(self, identifier: str) -> KillChainPhase | None:
        """This function will find KillChainPhase by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for KillChainPhase to find

        Returns:
        --------
        KillChainPhase:
            The KillChainPhase

        """

        self._update_files_path()

        kill_chain_phase = None

        if self.exist_by_identifier(identifier):
            with open(
                f"{self.__files_path}/{self._generate_id(identifier)}.json",
                "r",
            ) as file:
                kill_chain_phase_dto = KillChainPhaseDTO()
                kill_chain_phase_dto.from_stix21(file.read())
                kill_chain_phase = self._convert_to_entity(
                    kill_chain_phase_dto
                )

        return kill_chain_phase

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete KillChainPhase

        Parameters:
        -----------
        identifier: str
            The identifier for the KillChainPhase to delete

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
        self, kill_chain_phase: KillChainPhase
    ) -> KillChainPhaseDTO:
        """This function will convert KillChainPhase to a KillChainPhaseDTO

        Parameters:
        -----------
        kill_chain_phase: KillChainPhase
            Entity KillChainPhase as seen by the core

        Returns:
        --------
        KillChainPhaseDTO
            the KillChainPhaseDTO ready to be persist

        """

        identifier = (
            kill_chain_phase.kill_chain_name,
            kill_chain_phase.phase_name,
        )

        kill_chain_phase_dto = KillChainPhaseDTO()
        kill_chain_phase_dto.id = self._generate_id(identifier)
        kill_chain_phase_dto.kill_chain_name = kill_chain_phase.kill_chain_name
        kill_chain_phase_dto.phase_name = kill_chain_phase.phase_name

        return kill_chain_phase_dto

    def _convert_to_entity(
        self, kill_chain_phase_dto: KillChainPhaseDTO
    ) -> KillChainPhase:
        """This function will convert a KillChainPhaseDTO to KillChainPhase

        Parameters:
        -----------
        KillChainPhaseDTO
            the KillChainPhaseDTO ready to be persist

        Returns:
        --------
        kill_chain_phase: KillChainPhase
            Entity KillChainPhase as seen by the core

        """

        kill_chain_phase = KillChainPhase()
        kill_chain_phase.kill_chain_name = kill_chain_phase_dto.kill_chain_name
        kill_chain_phase.phase_name = kill_chain_phase_dto.phase_name
        kill_chain_phase.stix_representation = kill_chain_phase_dto.to_stix21()

        return kill_chain_phase
