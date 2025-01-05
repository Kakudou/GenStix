"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_inputport import (
    ListAttackPatternInputPort,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_outputport_builder import (
    ListAttackPatternOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.list_attack_pattern.list_attack_pattern_outputport import (
    ListAttackPatternOutputPort,
)


@dataclass
class ListAttackPattern:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListAttackPatternOutputPort
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
        self.builder = ListAttackPatternOutputPortBuilder()

    def execute(
        self, inputp: ListAttackPatternInputPort
    ) -> ListAttackPatternOutputPort:
        """This function will from the inputport create a AttackPattern
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListAttackPatternInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListAttackPatternOutputPort:
            The output contract

        """

        executed = False
        attack_pattern = None
        error = None

        all_attack_patterns = self.gateway.find_all()

        if all_attack_patterns is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            attack_pattern = True

        if executed:
            self.__output = (
                self.builder.create()
                .with_all_attack_patterns(all_attack_patterns)
                .build()
            )

        elif not executed and attack_pattern is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
