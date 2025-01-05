"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.read_attack_pattern.read_attack_pattern_inputport import (
    ReadAttackPatternInputPort,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.read_attack_pattern.read_attack_pattern_outputport_builder import (
    ReadAttackPatternOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.read_attack_pattern.read_attack_pattern_outputport import (
    ReadAttackPatternOutputPort,
)


@dataclass
class ReadAttackPattern:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadAttackPatternOutputPort
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
        self.builder = ReadAttackPatternOutputPortBuilder()

    def execute(
        self, inputp: ReadAttackPatternInputPort
    ) -> ReadAttackPatternOutputPort:
        """This function will from the inputport create a AttackPattern
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadAttackPatternInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadAttackPatternOutputPort:
            The output contract

        """

        executed = False
        attack_pattern = None
        error = None

        type_ = inputp.type_
        name = inputp.name

        identifier = (type_, name)

        attack_pattern = self.gateway.find_by_identifier(identifier)

        if attack_pattern is not None:
            executed = True
        else:
            error = "This AttackPattern, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()

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
