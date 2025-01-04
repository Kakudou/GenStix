"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_inputport\
    import CreateExternalReferenceInputPort
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_outputport_builder\
    import CreateExternalReferenceOutputPortBuilder
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_outputport\
    import CreateExternalReferenceOutputPort
from gen_stix.src.gen_stix.entity.\
    cdts.external_reference.external_reference\
    import ExternalReference


@dataclass
class CreateExternalReference:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateExternalReferenceOutputPort
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
        self.builder = CreateExternalReferenceOutputPortBuilder()

    def execute(self, inputp: CreateExternalReferenceInputPort) -> CreateExternalReferenceOutputPort:
        """This function will from the inputport create a ExternalReference
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateExternalReferenceInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateExternalReferenceOutputPort:
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

        external_reference = self.gateway.exist_by_identifier(identifier)

        if external_reference:
            error = "The ExternalReference you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            external_reference = ExternalReference()
            external_reference.source_name = source_name
            external_reference.description = description
            external_reference.url = url
            external_reference.hashes = hashes
            external_reference.external_id = external_id

            executed = self.gateway.save(external_reference)

        if executed:
            self.__output = self.builder.create()\
                                .with_source_name(external_reference.source_name)\
                                .with_description(external_reference.description)\
                                .with_url(external_reference.url)\
                                .with_hashes(external_reference.hashes)\
                                .with_external_id(external_reference.external_id)\
                                .build()

        elif not executed and external_reference is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
