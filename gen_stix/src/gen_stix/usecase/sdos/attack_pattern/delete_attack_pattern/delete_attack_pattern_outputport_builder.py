"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_outputport import (
    DeleteAttackPatternOutputPort,
)


@dataclass
class DeleteAttackPatternOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: DeleteAttackPatternOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_deleted: bool
        fill the deleted in the contract
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
        DeleteAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = DeleteAttackPatternOutputPort()
        return self

    def with_deleted(self, deleted: bool):
        """This function fill the deleted in the contract

        Parameters:
        -----------
        deleted: bool
            the deleted of the DeleteAttackPattern

        Returns:
        --------
        DeleteAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.deleted = deleted
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        DeleteAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> DeleteAttackPatternOutputPort:
        """This function return the filled contract

        Returns:
        --------
        DeleteAttackPatternOutputPort
            the contract filled

        """

        return self.__output
