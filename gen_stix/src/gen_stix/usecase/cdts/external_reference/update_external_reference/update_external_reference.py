"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.external_reference.update_external_reference.update_external_reference_inputport import (
    UpdateExternalReferenceInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.update_external_reference.update_external_reference_outputport_builder import (
    UpdateExternalReferenceOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.external_reference.update_external_reference.update_external_reference_outputport import (
    UpdateExternalReferenceOutputPort,
)


@dataclass
class UpdateExternalReference:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateExternalReferenceOutputPort
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
        self.builder = UpdateExternalReferenceOutputPortBuilder()

    def execute(
        self, inputp: UpdateExternalReferenceInputPort
    ) -> UpdateExternalReferenceOutputPort:
        """This function will from the inputport create a ExternalReference
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateExternalReferenceInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateExternalReferenceOutputPort:
            The output contract

        """

        executed = False
        external_reference = None
        error = None

        source_name = inputp.source_name
        description = inputp.description
        url = inputp.url
        hashes = inputp.hashes
        external_id = inputp.external_id

        identifier = (source_name, external_id)

        external_reference = self.gateway.find_by_identifier(identifier)

        if external_reference is None:
            error = (
                "The ExternalReference you want, doesn't look like to exist"
            )
            self.__output = self.builder.create().with_error(error).build()
        else:
            external_reference.source_name = source_name
            external_reference.description = description
            external_reference.url = url
            external_reference.hashes = hashes
            external_reference.external_id = external_id

            executed = self.gateway.update_by_identifier(
                identifier, external_reference
            )

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
