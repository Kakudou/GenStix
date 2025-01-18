"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.update_kill_chain_phase.update_kill_chain_phase_inputport import (
    UpdateKillChainPhaseInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.update_kill_chain_phase.update_kill_chain_phase_outputport_builder import (
    UpdateKillChainPhaseOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.update_kill_chain_phase.update_kill_chain_phase_outputport import (
    UpdateKillChainPhaseOutputPort,
)


@dataclass
class UpdateKillChainPhase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateKillChainPhaseOutputPort
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
        self.builder = UpdateKillChainPhaseOutputPortBuilder()

    def execute(
        self, inputp: UpdateKillChainPhaseInputPort
    ) -> UpdateKillChainPhaseOutputPort:
        """This function will from the inputport create a KillChainPhase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateKillChainPhaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateKillChainPhaseOutputPort:
            The output contract

        """

        executed = False
        kill_chain_phase = None
        error = None

        kill_chain_name = inputp.kill_chain_name
        phase_name = inputp.phase_name

        identifier = (kill_chain_name, phase_name)

        kill_chain_phase = self.gateway.find_by_identifier(identifier)

        if kill_chain_phase is None:
            error = "The KillChainPhase you want, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            kill_chain_phase.kill_chain_name = kill_chain_name
            kill_chain_phase.phase_name = phase_name

            executed = self.gateway.update_by_identifier(
                identifier, kill_chain_phase
            )

        if executed:
            self.__output = (
                self.builder.create()
                .with_kill_chain_name(kill_chain_phase.kill_chain_name)
                .with_phase_name(kill_chain_phase.phase_name)
                .with_stix_representation(kill_chain_phase.stix_representation)
                .build()
            )

        elif not executed and kill_chain_phase is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
