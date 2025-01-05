"""This module handle the data access in memory"""

from hashlib import sha256
from typing import List

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
from gen_stix.src.app.repository.inmemory.inmemory_persist import (
    InMemoryPersist,
)


@Singleton
class KillChainPhaseINMEMORYRepository(KillChainPhaseGateway):
    """ "This class implement the KillChainPhaseGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the KillChainPhase inmemory dict
    exist_by_identifier:
        will check if an KillChainPhase with this identifier exist
    update_by_identifier:
        will 'update' the KillChainPhase inmemory dict
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
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.kill_chain_phases = {}

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

        saved = False

        kill_chain_phase_dto = self._convert_to_dto(kill_chain_phase)
        self.__persists.kill_chain_phases[kill_chain_phase_dto.id] = (
            kill_chain_phase_dto
        )

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

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.kill_chain_phases[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

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

        updated = False

        kill_chain_phase_dto = self._convert_to_dto(kill_chain_phase)
        self.__persists.kill_chain_phases[kill_chain_phase_dto.id] = (
            kill_chain_phase_dto
        )

        updated = True

        return updated

    def find_all(self) -> List[KillChainPhase]:
        """This function will find all KillChainPhase

        Parameters:
        -----------

        Returns:
        --------
        List[KillChainPhase]:
            all KillChainPhase

        """

        kill_chain_phases = []
        for kill_chain_phase_id in self.__persists.kill_chain_phases:
            kill_chain_phase_dto = self.__persists.kill_chain_phases[
                kill_chain_phase_id
            ]
            kill_chain_phase = self._convert_to_entity(kill_chain_phase_dto)
            kill_chain_phases.append(kill_chain_phase)

        return kill_chain_phases

    def find_by_identifier(self, identifier: str) -> KillChainPhase:
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

        kill_chain_phase = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            kill_chain_phase_dto = self.__persists.kill_chain_phases[hash_id]
        except KeyError:
            kill_chain_phase_dto = None

        if kill_chain_phase_dto is not None:
            kill_chain_phase = self._convert_to_entity(kill_chain_phase_dto)

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

        deleted = False

        kill_chain_phase_id = self._generate_id(identifier)
        del self.__persists.kill_chain_phases[kill_chain_phase_id]

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

        return kill_chain_phase
