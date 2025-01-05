"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_inputport import (
    ReadExternalReferenceInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_outputport_builder import (
    ReadExternalReferenceOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_outputport import (
    ReadExternalReferenceOutputPort,
)


@dataclass
class ReadExternalReference:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadExternalReferenceOutputPort
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
        self.builder = ReadExternalReferenceOutputPortBuilder()

    def execute(
        self, inputp: ReadExternalReferenceInputPort
    ) -> ReadExternalReferenceOutputPort:
        """This function will from the inputport create a ExternalReference
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadExternalReferenceInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadExternalReferenceOutputPort:
            The output contract

        """

        executed = False
        external_reference = None
        error = None

        source_name = inputp.source_name
        external_id = inputp.external_id

        identifier = (source_name, external_id)

        external_reference = self.gateway.find_by_identifier(identifier)

        if external_reference is not None:
            executed = True
        else:
            error = "This ExternalReference, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()

        if executed:
            self.__output = (
                self.builder.create()
                .with_source_name(external_reference.source_name)
                .with_description(external_reference.description)
                .with_url(external_reference.url)
                .with_hashes(external_reference.hashes)
                .with_external_id(external_reference.external_id)
                .build()
            )

        elif not executed and external_reference is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
