""" This module use the usecase CreateExternalReference"""
from typing\
    import Dict

from gen_stix.src\
    import STORAGE_ENGINE

from gen_stix.src.utils.container\
    import Container
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.create_external_reference.create_external_reference_inputport_builder\
    import CreateExternalReferenceInputPortBuilder


class CreateExternalReferenceAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase CreateExternalReference.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into CreateExternalReferenceInputPort
        with the use of CreateExternalReferenceInputPortBuilder.
        Then this contract will be gave to CreateExternalReference usecase.
        In return we should obtain the contract CreateExternalReferenceOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            source_name: str
                The name of the source that the external-reference is defined within (system, registry, organization, etc.).
            description: str
                A human readable description.
            url: str
                A URL reference to an external resource [RFC3986].
            hashes: Dict
                Specifies a dictionary of hashes for the contents of the url. This SHOULD be provided when the url property is present. Dictionary keys MUST come from one of the entries listed in the hash-algorithm-ov open vocabulary. As stated in Section 2.7, to ensure interoperability, a SHA-256 hash SHOULD be included whenever possible.
            external_id: str
                An identifier for the external reference content.

        Returns:
        --------
        CreateExternalReference_oc
            the output contract of the usecase CreateExternalReference

        """

        sanitize_source_name = inputs["source_name"]
        sanitize_description = inputs["description"]
        sanitize_url = inputs["url"]
        sanitize_hashes = inputs["hashes"]
        sanitize_external_id = inputs["external_id"]

        create_external_reference_icb = CreateExternalReferenceInputPortBuilder()
        create_external_reference_ic = create_external_reference_icb\
            .create()\
            .with_source_name(sanitize_source_name)\
            .with_description(sanitize_description)\
            .with_url(sanitize_url)\
            .with_hashes(sanitize_hashes)\
            .with_external_id(sanitize_external_id)\
            .build()

        create_external_reference_oc = Container\
            .get_usecase_repo("CreateExternalReference", storage_engine)\
            .execute(create_external_reference_ic)

        return create_external_reference_oc
