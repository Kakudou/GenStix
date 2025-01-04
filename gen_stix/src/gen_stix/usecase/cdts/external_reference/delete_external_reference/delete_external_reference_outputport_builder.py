"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.delete_external_reference.delete_external_reference_outputport\
    import DeleteExternalReferenceOutputPort


@dataclass
class DeleteExternalReferenceOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: DeleteExternalReferenceOutputPort
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
        """ This function create the empty contract

        Returns:
        --------
        DeleteExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = DeleteExternalReferenceOutputPort()
        return self

    def with_deleted(self, deleted: bool):
        """ This function fill the deleted in the contract

        Parameters:
        -----------
        deleted: bool
            the deleted of the DeleteExternalReference

        Returns:
        --------
        DeleteExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.deleted = deleted
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        DeleteExternalReferenceOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> DeleteExternalReferenceOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteExternalReferenceOutputPort
            the contract filled

        """

        return self.__output
