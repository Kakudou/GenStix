""" This module use the usecase DeleteAttackPattern"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_inputport_builder import (
    DeleteAttackPatternInputPortBuilder,
)


class DeleteAttackPatternAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteAttackPattern.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteAttackPatternInputPort
        with the use of DeleteAttackPatternInputPortBuilder.
        Then this contract will be gave to DeleteAttackPattern usecase.
        In return we should obtain the contract DeleteAttackPatternOutputPort

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
        DeleteAttackPattern_oc
            the output contract of the usecase DeleteAttackPattern

        """

        sanitize_type_ = inputs["type_"]
        sanitize_name = inputs["name"]

        delete_attack_pattern_icb = DeleteAttackPatternInputPortBuilder()
        delete_attack_pattern_ic = (
            delete_attack_pattern_icb.create()
            .with_type_(sanitize_type_)
            .with_name(sanitize_name)
            .build()
        )

        delete_attack_pattern_oc = Container.get_usecase_repo(
            "DeleteAttackPattern", storage_engine
        ).execute(delete_attack_pattern_ic)

        return delete_attack_pattern_oc
