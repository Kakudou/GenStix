""" This module use the usecase DeleteExternalReference"""
from typing\
    import Dict

from gen_stix.src\
    import STORAGE_ENGINE

from gen_stix.src.utils.container\
    import Container
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.delete_external_reference.delete_external_reference_inputport_builder\
    import DeleteExternalReferenceInputPortBuilder


class DeleteExternalReferenceAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteExternalReference.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteExternalReferenceInputPort
        with the use of DeleteExternalReferenceInputPortBuilder.
        Then this contract will be gave to DeleteExternalReference usecase.
        In return we should obtain the contract DeleteExternalReferenceOutputPort

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
        DeleteExternalReference_oc
            the output contract of the usecase DeleteExternalReference

        """

        sanitize_source_name = inputs["source_name"]
        sanitize_external_id = inputs["external_id"]

        delete_external_reference_icb = DeleteExternalReferenceInputPortBuilder()
        delete_external_reference_ic = delete_external_reference_icb\
            .create()\
            .with_source_name(sanitize_source_name)\
            .with_external_id(sanitize_external_id)\
            .build()

        delete_external_reference_oc = Container\
            .get_usecase_repo("DeleteExternalReference", storage_engine)\
            .execute(delete_external_reference_ic)

        return delete_external_reference_oc
