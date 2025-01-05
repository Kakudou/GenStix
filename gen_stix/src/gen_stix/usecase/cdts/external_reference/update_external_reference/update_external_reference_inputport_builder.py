"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any, Dict
from gen_stix.src.gen_stix.usecase.cdts.external_reference.update_external_reference.update_external_reference_inputport import (
    UpdateExternalReferenceInputPort,
)


@dataclass
class UpdateExternalReferenceInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: UpdateExternalReferenceInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
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
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        UpdateExternalReferenceInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = UpdateExternalReferenceInputPort()
        return self

    def with_source_name(self, source_name: str):
        """This function fill the source_name in the contract

        Parameters:
        -----------
        source_name: str
            the source_name of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
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
            the source_name of the UpdateExternalReference

        Returns:
        --------

        """

        if source_name is None or type == "":
            raise ValueError(
                "`source_name` is a required field for ExternalReference"
            )
        elif type(source_name) is not str:
            raise ValueError("`source_name` must be a str.")

    def with_description(self, description: str):
        """This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_description(description)
        self.__input.description = description
        return self

    def _validate_description(self, description: str):
        """This function check the  validity of description in the contract

        Parameters:
        -----------
        description: str
            the description of the UpdateExternalReference

        Returns:
        --------

        """

        if description is not None:
            if type(description) is not str:
                raise ValueError("`description` must be a str.")

    def with_url(self, url: str):
        """This function fill the url in the contract

        Parameters:
        -----------
        url: str
            the url of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_url(url)
        self.__input.url = url
        return self

    def _validate_url(self, url: str):
        """This function check the  validity of url in the contract

        Parameters:
        -----------
        url: str
            the url of the UpdateExternalReference

        Returns:
        --------

        """

        if url is not None:
            if type(url) is not str:
                raise ValueError("`url` must be a str.")

    def with_hashes(self, hashes: Dict):
        """This function fill the hashes in the contract

        Parameters:
        -----------
        hashes: Dict
            the hashes of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_hashes(hashes)
        self.__input.hashes = hashes
        return self

    def _validate_hashes(self, hashes: Dict):
        """This function check the  validity of hashes in the contract

        Parameters:
        -----------
        hashes: Dict
            the hashes of the UpdateExternalReference

        Returns:
        --------

        """

        if hashes is not None:
            if not isinstance(hashes, Dict):
                raise ValueError("`hashes` must be a Dict.")

    def with_external_id(self, external_id: str):
        """This function fill the external_id in the contract

        Parameters:
        -----------
        external_id: str
            the external_id of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
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
            the external_id of the UpdateExternalReference

        Returns:
        --------

        """

        if external_id is not None:
            if type(external_id) is not str:
                raise ValueError("`external_id` must be a str.")
            if (
                self.__input.source_name == "capec"
                and not external_id.startswith("CAPEC-")
            ):
                raise ValueError(
                    "`external_id` with `source_name` 'capec' must be a CAPEC-[id]."
                )

    def build(self) -> UpdateExternalReferenceInputPort:
        """This function return the filled contract

        Returns:
        --------
        UpdateExternalReferenceInputPort
            the contract filled

        """

        self._validate_source_name(self.__input.source_name)
        self._validate_description(self.__input.description)
        self._validate_url(self.__input.url)
        self._validate_hashes(self.__input.hashes)
        self._validate_external_id(self.__input.external_id)

        return self.__input
