"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.external_reference.delete_external_reference.delete_external_reference_inputport import (
    DeleteExternalReferenceInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.delete_external_reference.delete_external_reference_outputport_builder import (
    DeleteExternalReferenceOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.delete_external_reference.delete_external_reference_outputport import (
    DeleteExternalReferenceOutputPort,
)


@dataclass
class DeleteExternalReference:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteExternalReferenceOutputPort
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
        self.builder = DeleteExternalReferenceOutputPortBuilder()

    def execute(
        self, inputp: DeleteExternalReferenceInputPort
    ) -> DeleteExternalReferenceOutputPort:
        """This function will from the inputport create a ExternalReference
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteExternalReferenceInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteExternalReferenceOutputPort:
            The output contract

        """

        executed = False
        external_reference = None
        error = None

        source_name = inputp.source_name
        external_id = inputp.external_id

        identifier = (source_name, external_id)

        external_reference_deleted = self.gateway.destroy_by_identifier(
            identifier
        )

        if external_reference_deleted:
            error = "This Entity ExternalReference, doesn't look like to exist in GenSTIX"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            external_reference = True

        if executed:
            self.__output = (
                self.builder.create()
                .with_deleted(external_reference_deleted)
                .build()
            )

        elif not executed and external_reference is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
