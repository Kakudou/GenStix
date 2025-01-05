"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_inputport import (
    DeleteKillChainPhaseInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_outputport_builder import (
    DeleteKillChainPhaseOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_outputport import (
    DeleteKillChainPhaseOutputPort,
)


@dataclass
class DeleteKillChainPhase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteKillChainPhaseOutputPort
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
        self.builder = DeleteKillChainPhaseOutputPortBuilder()

    def execute(
        self, inputp: DeleteKillChainPhaseInputPort
    ) -> DeleteKillChainPhaseOutputPort:
        """This function will from the inputport create a KillChainPhase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteKillChainPhaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteKillChainPhaseOutputPort:
            The output contract

        """

        executed = False
        kill_chain_phase = None
        error = None

        kill_chain_name = inputp.kill_chain_name
        phase_name = inputp.phase_name

        identifier = (kill_chain_name, phase_name)

        kill_chain_phase_deleted = self.gateway.destroy_by_identifier(
            identifier
        )

        if kill_chain_phase_deleted:
            error = "This Entity KillChainPhase, doesn't look like to exist in GenSTIX"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            kill_chain_phase = True

        if executed:
            self.__output = (
                self.builder.create()
                .with_deleted(kill_chain_phase_deleted)
                .build()
            )

        elif not executed and kill_chain_phase is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
