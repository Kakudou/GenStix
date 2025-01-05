"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any, List
from gen_stix.src.gen_stix.usecase.cdts.external_reference.list_external_reference.list_external_reference_outputport import (
    ListExternalReferenceOutputPort,
)


@dataclass
class ListExternalReferenceOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListExternalReferenceOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_external_references: List[str]
        fill the all_external_references in the contract
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
        ListExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListExternalReferenceOutputPort()
        return self

    def with_all_external_references(self, all_external_references: List[str]):
        """This function fill the all_external_references in the contract

        Parameters:
        -----------
        all_external_references: List[str]
            the all_external_references of the ListExternalReference

        Returns:
        --------
        ListExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_external_references = all_external_references
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListExternalReferenceOutputPort:
        """This function return the filled contract

        Returns:
        --------
        ListExternalReferenceOutputPort
            the contract filled

        """

        return self.__output
