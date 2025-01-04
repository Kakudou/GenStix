""" This module use the usecase ListExternalReference"""
from typing\
    import Dict

from gen_stix.src\
    import STORAGE_ENGINE

from gen_stix.src.utils.container\
    import Container
from gen_stix.src.gen_stix.usecase.\
    cdts.external_reference.list_external_reference.list_external_reference_inputport_builder\
    import ListExternalReferenceInputPortBuilder


class ListExternalReferenceAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListExternalReference.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListExternalReferenceInputPort
        with the use of ListExternalReferenceInputPortBuilder.
        Then this contract will be gave to ListExternalReference usecase.
        In return we should obtain the contract ListExternalReferenceOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListExternalReference_oc
            the output contract of the usecase ListExternalReference

        """

        list_external_reference_icb = ListExternalReferenceInputPortBuilder()
        list_external_reference_ic = list_external_reference_icb\
            .create()\
            .build()

        list_external_reference_oc = Container\
            .get_usecase_repo("ListExternalReference", storage_engine)\
            .execute(list_external_reference_ic)

        return list_external_reference_oc
