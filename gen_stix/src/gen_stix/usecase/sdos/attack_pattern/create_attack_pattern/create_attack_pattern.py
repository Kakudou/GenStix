"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport import (
    CreateAttackPatternInputPort,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_outputport_builder import (
    CreateAttackPatternOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_outputport import (
    CreateAttackPatternOutputPort,
)
from gen_stix.src.gen_stix.entity.sdos.attack_pattern.attack_pattern import (
    AttackPattern,
)


@dataclass
class CreateAttackPattern:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateAttackPatternOutputPort
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
        self.builder = CreateAttackPatternOutputPortBuilder()

    def execute(
        self, inputp: CreateAttackPatternInputPort
    ) -> CreateAttackPatternOutputPort:
        """This function will from the inputport create a AttackPattern
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateAttackPatternInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateAttackPatternOutputPort:
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

        attack_pattern = self.gateway.exist_by_identifier(identifier)

        if attack_pattern:
            error = "The AttackPattern you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            attack_pattern = AttackPattern()
            attack_pattern.type_ = type_
            attack_pattern.external_references = external_references
            attack_pattern.name = name
            attack_pattern.description = description
            attack_pattern.aliases = aliases
            attack_pattern.kill_chain_phases = kill_chain_phases

            executed = self.gateway.save(attack_pattern)

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
