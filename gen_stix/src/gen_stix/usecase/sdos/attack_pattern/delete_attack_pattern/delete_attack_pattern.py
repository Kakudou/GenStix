"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_inputport import (
    DeleteAttackPatternInputPort,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_outputport_builder import (
    DeleteAttackPatternOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.delete_attack_pattern.delete_attack_pattern_outputport import (
    DeleteAttackPatternOutputPort,
)


@dataclass
class DeleteAttackPattern:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteAttackPatternOutputPort
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
        self.builder = DeleteAttackPatternOutputPortBuilder()

    def execute(
        self, inputp: DeleteAttackPatternInputPort
    ) -> DeleteAttackPatternOutputPort:
        """This function will from the inputport create a AttackPattern
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteAttackPatternInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteAttackPatternOutputPort:
            The output contract

        """

        executed = False
        attack_pattern = None
        error = None

        type_ = inputp.type_
        name = inputp.name

        identifier = (type_, name)

        attack_pattern_deleted = self.gateway.destroy_by_identifier(identifier)

        if attack_pattern_deleted:
            error = "This Entity AttackPattern, doesn't look like to exist in GenSTIX"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            attack_pattern = True

        if executed:
            self.__output = (
                self.builder.create()
                .with_deleted(attack_pattern_deleted)
                .build()
            )

        elif not executed and attack_pattern is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
