""" This module use the usecase CreateAttackPattern"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport_builder import (
    CreateAttackPatternInputPortBuilder,
)


class CreateAttackPatternAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase CreateAttackPattern.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into CreateAttackPatternInputPort
        with the use of CreateAttackPatternInputPortBuilder.
        Then this contract will be gave to CreateAttackPattern usecase.
        In return we should obtain the contract CreateAttackPatternOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            type_: str
                The value of this property **MUST** be attack-pattern.
            external_references: List
                A list of external references which refer to non-STIX information. This property MAY be used to provide one or more Attack Pattern identifiers, such as a CAPEC ID. When specifying a CAPEC ID, the source_name property of the external reference MUST be set to capec and the external_id property MUST be formatted as CAPEC-[id].
            name: str
                A name used to identify the Attack Pattern.
            description: str
                A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.
            aliases: List[str]
                Alternative names used to identify this Attack Pattern.
            kill_chain_phases: List
                The list of Kill Chain Phases for which this Attack Pattern is used.

        Returns:
        --------
        CreateAttackPattern_oc
            the output contract of the usecase CreateAttackPattern

        """

        sanitize_type_ = inputs["type_"]
        sanitize_external_references = inputs["external_references"]
        sanitize_name = inputs["name"]
        sanitize_description = inputs["description"]
        sanitize_aliases = inputs["aliases"]
        sanitize_kill_chain_phases = inputs["kill_chain_phases"]

        create_attack_pattern_icb = CreateAttackPatternInputPortBuilder()
        create_attack_pattern_ic = (
            create_attack_pattern_icb.create()
            .with_type_(sanitize_type_)
            .with_external_references(sanitize_external_references)
            .with_name(sanitize_name)
            .with_description(sanitize_description)
            .with_aliases(sanitize_aliases)
            .with_kill_chain_phases(sanitize_kill_chain_phases)
            .build()
        )

        create_attack_pattern_oc = Container.get_usecase_repo(
            "CreateAttackPattern", storage_engine
        ).execute(create_attack_pattern_ic)

        return create_attack_pattern_oc
