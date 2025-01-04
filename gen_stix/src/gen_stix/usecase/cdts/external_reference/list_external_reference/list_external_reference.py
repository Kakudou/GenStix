"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.list_external_reference.list_external_reference_inputport\
    import ListExternalReferenceInputPort
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.list_external_reference.list_external_reference_outputport_builder\
    import ListExternalReferenceOutputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.list_external_reference.list_external_reference_outputport\
    import ListExternalReferenceOutputPort


@dataclass
class ListExternalReference:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListExternalReferenceOutputPort
        is the outputport information who gonna travel to the adapter

    Functions:
    ----------
    __init__:
        classical constructor
    execute:
        execute the usecase logic

    """

    __output: Any = None

    def __init__(self, implemented_gateway):
        """This function is the constructor particularity:
        the container utils class give it the good implemented_gateway

        Parameters:
        -----------
        implemented_gateway:
            The implemented_gateway for the storage engine we want
        """

        self.gateway = implemented_gateway
        self.builder = ListExternalReferenceOutputPortBuilder()

    def execute(self, inputp: ListExternalReferenceInputPort) -> ListExternalReferenceOutputPort:
        """This function will from the inputport create a ExternalReference
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListExternalReferenceInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListExternalReferenceOutputPort:
            The output contract

        """

        executed = False
        external_reference = None
        error = None

        all_external_references = self.gateway.find_all()

        if all_external_references is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            external_reference = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_external_references(all_external_references)\
                                .build()

        elif not executed and external_reference is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
