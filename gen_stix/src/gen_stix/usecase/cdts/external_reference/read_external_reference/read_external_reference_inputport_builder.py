"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_inputport import (
    ReadExternalReferenceInputPort,
)

from gen_stix.src.gen_stix.entity.enums.external_reference_capec import (
    ExternalReferenceCapec,
)


@dataclass
class ReadExternalReferenceInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ReadExternalReferenceInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_source_name: str
        fill the source_name in the contract
    with_external_id: str
        fill the external_id in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        ReadExternalReferenceInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ReadExternalReferenceInputPort()
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

        self._validate_source_name(source_name)
        self.__input.source_name = source_name
        return self

    def _validate_source_name(self, source_name: str):
        """This function check the  validity of source_name in the contract

        Parameters:
        -----------
        source_name: str
            the source_name of the ReadExternalReference

        Returns:
        --------

        """

        if source_name is None or source_name == "":
            raise ValueError(
                "`source_name` is a required field for ExternalReference"
            )
        elif type(source_name) is not str:
            raise ValueError("`source_name` must be a str.")

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

        self._validate_external_id(external_id)
        self.__input.external_id = external_id
        return self

    def _validate_external_id(self, external_id: str):
        """This function check the  validity of external_id in the contract

        Parameters:
        -----------
        external_id: str
            the external_id of the ReadExternalReference

        Returns:
        --------

        """

        if external_id is not None:
            if type(external_id) is not str:
                raise ValueError("`external_id` must be a str.")
            if self.__input.source_name == "capec":
                if external_id.lower().startswith("capec-"):
                    external_id = external_id
                else:
                    ExternalReferenceCapec.from_name(external_id)

    def build(self) -> ReadExternalReferenceInputPort:
        """This function return the filled contract

        Returns:
        --------
        ReadExternalReferenceInputPort
            the contract filled

        """

        self._validate_source_name(self.__input.source_name)
        self._validate_external_id(self.__input.external_id)

        return self.__input
