"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any, List
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.read_attack_pattern.read_attack_pattern_outputport import (
    ReadAttackPatternOutputPort,
)


@dataclass
class ReadAttackPatternOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ReadAttackPatternOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_type_: str
        fill the type_ in the contract
    with_external_references: List
        fill the external_references in the contract
    with_name: str
        fill the name in the contract
    with_description: str
        fill the description in the contract
    with_aliases: List[str]
        fill the aliases in the contract
    with_kill_chain_phases: List
        fill the kill_chain_phases in the contract
    with_error:
        fill the possible usecase error
    build:
        build the final output contract

    """

    __output: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ReadAttackPatternOutputPort()
        return self

    def with_type_(self, type_: str):
        """This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.type_ = type_
        return self

    def with_external_references(self, external_references: List):
        """This function fill the external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.external_references = external_references
        return self

    def with_name(self, name: str):
        """This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.name = name
        return self

    def with_description(self, description: str):
        """This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.description = description
        return self

    def with_aliases(self, aliases: List[str]):
        """This function fill the aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.aliases = aliases
        return self

    def with_kill_chain_phases(self, kill_chain_phases: List):
        """This function fill the kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the ReadAttackPattern

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.kill_chain_phases = kill_chain_phases
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ReadAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ReadAttackPatternOutputPort:
        """This function return the filled contract

        Returns:
        --------
        ReadAttackPatternOutputPort
            the contract filled

        """

        return self.__output
