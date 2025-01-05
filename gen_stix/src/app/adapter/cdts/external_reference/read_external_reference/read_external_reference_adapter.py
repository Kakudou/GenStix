""" This module use the usecase ReadExternalReference"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.cdts.external_reference.read_external_reference.read_external_reference_inputport_builder import (
    ReadExternalReferenceInputPortBuilder,
)


class ReadExternalReferenceAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadExternalReference.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadExternalReferenceInputPort
        with the use of ReadExternalReferenceInputPortBuilder.
        Then this contract will be gave to ReadExternalReference usecase.
        In return we should obtain the contract ReadExternalReferenceOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            source_name: str
                The name of the source that the external-reference is defined within (system, registry, organization, etc.).
            external_id: str
                An identifier for the external reference content.

        Returns:
        --------
        ReadExternalReference_oc
            the output contract of the usecase ReadExternalReference

        """

        sanitize_source_name = inputs["source_name"]
        sanitize_external_id = inputs["external_id"]

        read_external_reference_icb = ReadExternalReferenceInputPortBuilder()
        read_external_reference_ic = (
            read_external_reference_icb.create()
            .with_source_name(sanitize_source_name)
            .with_external_id(sanitize_external_id)
            .build()
        )

        read_external_reference_oc = Container.get_usecase_repo(
            "ReadExternalReference", storage_engine
        ).execute(read_external_reference_ic)

        return read_external_reference_oc
