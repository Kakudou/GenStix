"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.read_kill_chain_phase.read_kill_chain_phase_inputport import (
    ReadKillChainPhaseInputPort,
)


@dataclass
class ReadKillChainPhaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ReadKillChainPhaseInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_kill_chain_name: str
        fill the kill_chain_name in the contract
    with_phase_name: str
        fill the phase_name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        ReadKillChainPhaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ReadKillChainPhaseInputPort()
        return self

    def with_kill_chain_name(self, kill_chain_name: str):
        """This function fill the kill_chain_name in the contract

        Parameters:
        -----------
        kill_chain_name: str
            the kill_chain_name of the ReadKillChainPhase

        Returns:
        --------
        ReadKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_kill_chain_name(kill_chain_name)
        self.__input.kill_chain_name = kill_chain_name
        return self

    def _validate_kill_chain_name(self, kill_chain_name: str):
        """This function check the  validity of kill_chain_name in the contract

        Parameters:
        -----------
        kill_chain_name: str
            the kill_chain_name of the ReadKillChainPhase

        Returns:
        --------

        """
        raise NotImplementedError

    def with_phase_name(self, phase_name: str):
        """This function fill the phase_name in the contract

        Parameters:
        -----------
        phase_name: str
            the phase_name of the ReadKillChainPhase

        Returns:
        --------
        ReadKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_phase_name(phase_name)
        self.__input.phase_name = phase_name
        return self

    def _validate_phase_name(self, phase_name: str):
        """This function check the  validity of phase_name in the contract

        Parameters:
        -----------
        phase_name: str
            the phase_name of the ReadKillChainPhase

        Returns:
        --------

        """
        raise NotImplementedError

    def build(self) -> ReadKillChainPhaseInputPort:
        """This function return the filled contract

        Returns:
        --------
        ReadKillChainPhaseInputPort
            the contract filled

        """

        self._validate_kill_chain_name(self.__input.kill_chain_name)
        self._validate_phase_name(self.__input.phase_name)

        return self.__input
