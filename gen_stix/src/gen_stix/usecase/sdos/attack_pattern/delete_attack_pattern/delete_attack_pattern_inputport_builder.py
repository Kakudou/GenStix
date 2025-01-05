"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_inputport import (
    DeleteAttackPatternInputPort,
)


@dataclass
class DeleteAttackPatternInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: DeleteAttackPatternInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_type_: str
        fill the type_ in the contract
    with_name: str
        fill the name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        DeleteAttackPatternInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = DeleteAttackPatternInputPort()
        return self

    def with_type_(self, type_: str):
        """This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the DeleteAttackPattern

        Returns:
        --------
        DeleteAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_type_(type_)
        self.__input.type_ = type_
        return self

    def _validate_type_(self, type_: str):
        """This function check the  validity of type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the DeleteAttackPattern

        Returns:
        --------

        """

        if type_ is None or type == "":
            raise ValueError("`type` is a required field for AttackPattern")
        elif type_ != "attack-pattern":
            raise ValueError("`type` must be `attack-pattern`.")

    def with_name(self, name: str):
        """This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the DeleteAttackPattern

        Returns:
        --------
        DeleteAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_name(name)
        self.__input.name = name
        return self

    def _validate_name(self, name: str):
        """This function check the  validity of name in the contract

        Parameters:
        -----------
        name: str
            the name of the DeleteAttackPattern

        Returns:
        --------

        """

        if name is None or name == "":
            raise ValueError("`name` is a required field for AttackPattern")
        elif type(name) is not str:
            raise ValueError("`name` must be a str.")

    def build(self) -> DeleteAttackPatternInputPort:
        """This function return the filled contract

        Returns:
        --------
        DeleteAttackPatternInputPort
            the contract filled

        """

        self._validate_type_(self.__input.type_)
        self._validate_name(self.__input.name)

        return self.__input
