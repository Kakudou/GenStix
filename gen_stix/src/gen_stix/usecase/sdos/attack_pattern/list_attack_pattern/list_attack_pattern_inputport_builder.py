"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_inputport import (
    ListAttackPatternInputPort,
)


@dataclass
class ListAttackPatternInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListAttackPatternInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        ListAttackPatternInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListAttackPatternInputPort()
        return self

    def build(self) -> ListAttackPatternInputPort:
        """This function return the filled contract

        Returns:
        --------
        ListAttackPatternInputPort
            the contract filled

        """

        return self.__input
