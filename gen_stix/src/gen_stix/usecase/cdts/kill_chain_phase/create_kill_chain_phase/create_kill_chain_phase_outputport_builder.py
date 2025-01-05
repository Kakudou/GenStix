"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_outputport import (
    CreateKillChainPhaseOutputPort,
)


@dataclass
class CreateKillChainPhaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: CreateKillChainPhaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_kill_chain_name: str
        fill the kill_chain_name in the contract
    with_phase_name: str
        fill the phase_name in the contract
    with_error:
        fill the possible usecase error
    build:
        build the final output contract

    """

    __output: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        CreateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = CreateKillChainPhaseOutputPort()
        return self

    def with_kill_chain_name(self, kill_chain_name: str):
        """This function fill the kill_chain_name in the contract

        Parameters:
        -----------
        kill_chain_name: str
            the kill_chain_name of the CreateKillChainPhase

        Returns:
        --------
        CreateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.kill_chain_name = kill_chain_name
        return self

    def with_phase_name(self, phase_name: str):
        """This function fill the phase_name in the contract

        Parameters:
        -----------
        phase_name: str
            the phase_name of the CreateKillChainPhase

        Returns:
        --------
        CreateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.phase_name = phase_name
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        CreateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> CreateKillChainPhaseOutputPort:
        """This function return the filled contract

        Returns:
        --------
        CreateKillChainPhaseOutputPort
            the contract filled

        """

        return self.__output
