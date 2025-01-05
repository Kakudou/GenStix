"""This module handle the data access in memory"""

from hashlib import sha256
from typing import List

from gen_stix.src.utils.singleton import Singleton
from gen_stix.src.app.dto.sdos.attack_pattern.attack_pattern_dto import (
    AttackPatternDTO,
)
from gen_stix.src.gen_stix.gateway.sdos.attack_pattern.attack_pattern_gateway import (
    AttackPatternGateway,
)
from gen_stix.src.gen_stix.entity.sdos.attack_pattern.attack_pattern import (
    AttackPattern,
)
from gen_stix.src.app.repository.inmemory.inmemory_persist import (
    InMemoryPersist,
)


@Singleton
class AttackPatternINMEMORYRepository(AttackPatternGateway):
    """ "This class implement the AttackPatternGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the AttackPattern inmemory dict
    exist_by_identifier:
        will check if an AttackPattern with this identifier exist
    update_by_identifier:
        will 'update' the AttackPattern inmemory dict
    find_all:
        will search all AttackPattern
    find_by_identifier:
        will search an AttackPattern by his identifier
    destroy_by_identifier:
        will delete an AttackPattern by his identifier
    _convert_to_dto:
        convert core AttackPattern to AttackPatternDTO
    _convert_to_entity:
        convert AttackPatternDTO to core AttackPattern
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.attack_patterns = {}

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

    def save(self, attack_pattern: AttackPattern) -> bool:
        """This function will save AttackPattern as AttackPatternDTO

        Parameters:
        -----------
        attack_pattern: AttackPattern
            The AttackPattern that we will be saved and convert as AttackPatternDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        attack_pattern_dto = self._convert_to_dto(attack_pattern)
        self.__persists.attack_patterns[attack_pattern_dto.id] = (
            attack_pattern_dto
        )

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check AttackPattern existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the AttackPattern to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.attack_patterns[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(
        self, identifier: str, attack_pattern: AttackPattern
    ) -> bool:
        """This function will update AttackPattern

        Parameters:
        -----------
        identifier: str
            the identifier for the AttackPattern to update
        attack_pattern: AttackPattern
            The AttackPattern that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        attack_pattern_dto = self._convert_to_dto(attack_pattern)
        self.__persists.attack_patterns[attack_pattern_dto.id] = (
            attack_pattern_dto
        )

        updated = True

        return updated

    def find_all(self) -> List[AttackPattern]:
        """This function will find all AttackPattern

        Parameters:
        -----------

        Returns:
        --------
        List[AttackPattern]:
            all AttackPattern

        """

        attack_patterns = []
        for attack_pattern_id in self.__persists.attack_patterns:
            attack_pattern_dto = self.__persists.attack_patterns[
                attack_pattern_id
            ]
            attack_pattern = self._convert_to_entity(attack_pattern_dto)
            attack_patterns.append(attack_pattern)

        return attack_patterns

    def find_by_identifier(self, identifier: str) -> AttackPattern:
        """This function will find AttackPattern by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for AttackPattern to find

        Returns:
        --------
        AttackPattern:
            The AttackPattern

        """

        attack_pattern = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            attack_pattern_dto = self.__persists.attack_patterns[hash_id]
        except KeyError:
            attack_pattern_dto = None

        if attack_pattern_dto is not None:
            attack_pattern = self._convert_to_entity(attack_pattern_dto)

        return attack_pattern

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete AttackPattern

        Parameters:
        -----------
        identifier: str
            The identifier for the AttackPattern to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        attack_pattern_id = self._generate_id(identifier)
        del self.__persists.attack_patterns[attack_pattern_id]

        deleted = True

        return deleted

    def _convert_to_dto(
        self, attack_pattern: AttackPattern
    ) -> AttackPatternDTO:
        """This function will convert AttackPattern to a AttackPatternDTO

        Parameters:
        -----------
        attack_pattern: AttackPattern
            Entity AttackPattern as seen by the core

        Returns:
        --------
        AttackPatternDTO
            the AttackPatternDTO ready to be persist

        """

        identifier = (attack_pattern.type_, attack_pattern.name)

        attack_pattern_dto = AttackPatternDTO()
        attack_pattern_dto.id = self._generate_id(identifier)
        attack_pattern_dto.type_ = attack_pattern.type_
        attack_pattern_dto.external_references = (
            attack_pattern.external_references
        )
        attack_pattern_dto.name = attack_pattern.name
        attack_pattern_dto.description = attack_pattern.description
        attack_pattern_dto.aliases = attack_pattern.aliases
        attack_pattern_dto.kill_chain_phases = attack_pattern.kill_chain_phases

        return attack_pattern_dto

    def _convert_to_entity(
        self, attack_pattern_dto: AttackPatternDTO
    ) -> AttackPattern:
        """This function will convert a AttackPatternDTO to AttackPattern

        Parameters:
        -----------
        AttackPatternDTO
            the AttackPatternDTO ready to be persist

        Returns:
        --------
        attack_pattern: AttackPattern
            Entity AttackPattern as seen by the core

        """

        attack_pattern = AttackPattern()
        attack_pattern.type_ = attack_pattern_dto.type_
        attack_pattern.external_references = (
            attack_pattern_dto.external_references
        )
        attack_pattern.name = attack_pattern_dto.name
        attack_pattern.description = attack_pattern_dto.description
        attack_pattern.aliases = attack_pattern_dto.aliases
        attack_pattern.kill_chain_phases = attack_pattern_dto.kill_chain_phases

        return attack_pattern
