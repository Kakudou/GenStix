"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.list_external_reference.list_external_reference_inputport\
    import ListExternalReferenceInputPort


@dataclass
class ListExternalReferenceInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListExternalReferenceInputPort
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
        """ This function create the empty contract

        Returns:
        --------
        ListExternalReferenceInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListExternalReferenceInputPort()
        return self

    def build(self) -> ListExternalReferenceInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListExternalReferenceInputPort
            the contract filled

        """

        return self.__input
