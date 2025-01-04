"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, Dict
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.update_external_reference.update_external_reference_outputport\
    import UpdateExternalReferenceOutputPort


@dataclass
class UpdateExternalReferenceOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: UpdateExternalReferenceOutputPort
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
    with_error:
        fill the possible usecase error
    build:
        build the final output contract

    """

    __output: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = UpdateExternalReferenceOutputPort()
        return self

    def with_source_name(self, source_name: str):
        """ This function fill the source_name in the contract

        Parameters:
        -----------
        source_name: str
            the source_name of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.source_name = source_name
        return self

    def with_description(self, description: str):
        """ This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.description = description
        return self

    def with_url(self, url: str):
        """ This function fill the url in the contract

        Parameters:
        -----------
        url: str
            the url of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.url = url
        return self

    def with_hashes(self, hashes: Dict):
        """ This function fill the hashes in the contract

        Parameters:
        -----------
        hashes: Dict
            the hashes of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.hashes = hashes
        return self

    def with_external_id(self, external_id: str):
        """ This function fill the external_id in the contract

        Parameters:
        -----------
        external_id: str
            the external_id of the UpdateExternalReference

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.external_id = external_id
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        UpdateExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> UpdateExternalReferenceOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        UpdateExternalReferenceOutputPort
            the contract filled

        """

        return self.__output
