"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any, Dict
from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_outputport import (
    ReadExternalReferenceOutputPort,
)


@dataclass
class ReadExternalReferenceOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ReadExternalReferenceOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_source_name: str
        fill the source_name in the contract
    with_description: str
        fill the description in the contract
    with_url: str
        fill the url in the contract
    with_hashes: Dict
        fill the hashes in the contract
    with_external_id: str
        fill the external_id in the contract
    with_stix_representation: dict
        fill the stix representation in the contract
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
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ReadExternalReferenceOutputPort()
        return self

    def with_source_name(self, source_name: str):
        """This function fill the source_name in the contract

        Parameters:
        -----------
        source_name: str
            the source_name of the ReadExternalReference

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.source_name = source_name
        return self

    def with_description(self, description: str):
        """This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the ReadExternalReference

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.description = description
        return self

    def with_url(self, url: str):
        """This function fill the url in the contract

        Parameters:
        -----------
        url: str
            the url of the ReadExternalReference

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.url = url
        return self

    def with_hashes(self, hashes: Dict):
        """This function fill the hashes in the contract

        Parameters:
        -----------
        hashes: Dict
            the hashes of the ReadExternalReference

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.hashes = hashes
        return self

    def with_external_id(self, external_id: str):
        """This function fill the external_id in the contract

        Parameters:
        -----------
        external_id: str
            the external_id of the ReadExternalReference

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.external_id = external_id
        return self

    def with_stix_representation(self, stix_representation: dict):
        """This function fill the stix representation in the contract

        Parameters:
        -----------
        stix_representation: dict
            the stix representation of the ExternalReference

        Returns:
        --------
        CreateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.stix_representation = stix_representation
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ReadExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ReadExternalReferenceOutputPort:
        """This function return the filled contract

        Returns:
        --------
        ReadExternalReferenceOutputPort
            the contract filled

        """

        return self.__output
