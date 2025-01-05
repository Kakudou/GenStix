""" This module use the usecase ReadAttackPattern"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.read_attack_pattern.read_attack_pattern_inputport_builder import (
    ReadAttackPatternInputPortBuilder,
)


class ReadAttackPatternAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadAttackPattern.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadAttackPatternInputPort
        with the use of ReadAttackPatternInputPortBuilder.
        Then this contract will be gave to ReadAttackPattern usecase.
        In return we should obtain the contract ReadAttackPatternOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            type_: str
                The value of this property **MUST** be attack-pattern.
            name: str
                A name used to identify the Attack Pattern.

        Returns:
        --------
        ReadAttackPattern_oc
            the output contract of the usecase ReadAttackPattern

        """

        sanitize_type_ = inputs["type_"]
        sanitize_name = inputs["name"]

        read_attack_pattern_icb = ReadAttackPatternInputPortBuilder()
        read_attack_pattern_ic = (
            read_attack_pattern_icb.create()
            .with_type_(sanitize_type_)
            .with_name(sanitize_name)
            .build()
        )

        read_attack_pattern_oc = Container.get_usecase_repo(
            "ReadAttackPattern", storage_engine
        ).execute(read_attack_pattern_ic)

        return read_attack_pattern_oc
