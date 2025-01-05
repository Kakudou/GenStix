"""This module is the core logic to create a Entity"""

from dataclasses import dataclass
from typing import Any

from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_inputport import (
    ListKillChainPhaseInputPort,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_outputport_builder import (
    ListKillChainPhaseOutputPortBuilder,
)
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_outputport import (
    ListKillChainPhaseOutputPort,
)


@dataclass
class ListKillChainPhase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListKillChainPhaseOutputPort
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
        self.builder = ListKillChainPhaseOutputPortBuilder()

    def execute(
        self, inputp: ListKillChainPhaseInputPort
    ) -> ListKillChainPhaseOutputPort:
        """This function will from the inputport create a KillChainPhase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListKillChainPhaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListKillChainPhaseOutputPort:
            The output contract

        """

        executed = False
        kill_chain_phase = None
        error = None

        all_kill_chain_phases = self.gateway.find_all()

        if all_kill_chain_phases is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            kill_chain_phase = True

        if executed:
            self.__output = (
                self.builder.create()
                .with_all_kill_chain_phases(all_kill_chain_phases)
                .build()
            )

        elif not executed and kill_chain_phase is None:
            if error is None:
                error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
