"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any, List
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_outputport import (
    ListAttackPatternOutputPort,
)


@dataclass
class ListAttackPatternOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListAttackPatternOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_attack_patterns: List[str]
        fill the all_attack_patterns in the contract
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
        ListAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListAttackPatternOutputPort()
        return self

    def with_all_attack_patterns(self, all_attack_patterns: List[str]):
        """This function fill the all_attack_patterns in the contract

        Parameters:
        -----------
        all_attack_patterns: List[str]
            the all_attack_patterns of the ListAttackPattern

        Returns:
        --------
        ListAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_attack_patterns = all_attack_patterns
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListAttackPatternOutputPort:
        """This function return the filled contract

        Returns:
        --------
        ListAttackPatternOutputPort
            the contract filled

        """

        return self.__output
