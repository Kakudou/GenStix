""" This module use the usecase ListAttackPattern"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_inputport_builder import (
    ListAttackPatternInputPortBuilder,
)


class ListAttackPatternAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListAttackPattern.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListAttackPatternInputPort
        with the use of ListAttackPatternInputPortBuilder.
        Then this contract will be gave to ListAttackPattern usecase.
        In return we should obtain the contract ListAttackPatternOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListAttackPattern_oc
            the output contract of the usecase ListAttackPattern

        """

        list_attack_pattern_icb = ListAttackPatternInputPortBuilder()
        list_attack_pattern_ic = list_attack_pattern_icb.create().build()

        list_attack_pattern_oc = Container.get_usecase_repo(
            "ListAttackPattern", storage_engine
        ).execute(list_attack_pattern_ic)

        return list_attack_pattern_oc
