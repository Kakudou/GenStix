"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.update_attack_pattern.update_attack_pattern_inputport import (
    UpdateAttackPatternInputPort,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.update_attack_pattern.update_attack_pattern_outputport_builder import (
    UpdateAttackPatternOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.update_attack_pattern.update_attack_pattern_outputport import (
    UpdateAttackPatternOutputPort,
)


@dataclass
class UpdateAttackPattern:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateAttackPatternOutputPort
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
        self.builder = UpdateAttackPatternOutputPortBuilder()

    def execute(
        self, inputp: UpdateAttackPatternInputPort
    ) -> UpdateAttackPatternOutputPort:
        """This function will from the inputport create a AttackPattern
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateAttackPatternInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateAttackPatternOutputPort:
            The output contract

        """

        executed = False
        attack_pattern = None
        error = None

        type_ = inputp.type_
        external_references = inputp.external_references
        name = inputp.name
        description = inputp.description
        aliases = inputp.aliases
        kill_chain_phases = inputp.kill_chain_phases

        identifier = (type_, name)

        attack_pattern = self.gateway.find_by_identifier(identifier)

        if attack_pattern is None:
            error = "The AttackPattern you want, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            attack_pattern.type_ = type_
            attack_pattern.external_references = external_references
            attack_pattern.name = name
            attack_pattern.description = description
            attack_pattern.aliases = aliases
            attack_pattern.kill_chain_phases = kill_chain_phases

            executed = self.gateway.update_by_identifier(
                identifier, attack_pattern
            )

        if executed:
            self.__output = (
                self.builder.create()
                .with_type_(attack_pattern.type_)
                .with_external_references(attack_pattern.external_references)
                .with_name(attack_pattern.name)
                .with_description(attack_pattern.description)
                .with_aliases(attack_pattern.aliases)
                .with_kill_chain_phases(attack_pattern.kill_chain_phases)
                .build()
            )

        elif not executed and attack_pattern is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
