"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.update_kill_chain_phase.update_kill_chain_phase_outputport import (
    UpdateKillChainPhaseOutputPort,
)


@dataclass
class UpdateKillChainPhaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: UpdateKillChainPhaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_kill_chain_name: str
        fill the kill_chain_name in the contract
    with_phase_name: str
        fill the phase_name in the contract
    with_stix_representation: dict
        fill the stix representation in the contract
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
        UpdateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = UpdateKillChainPhaseOutputPort()
        return self

    def with_kill_chain_name(self, kill_chain_name: str):
        """This function fill the kill_chain_name in the contract

        Parameters:
        -----------
        kill_chain_name: str
            the kill_chain_name of the UpdateKillChainPhase

        Returns:
        --------
        UpdateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.kill_chain_name = kill_chain_name
        return self

    def with_phase_name(self, phase_name: str):
        """This function fill the phase_name in the contract

        Parameters:
        -----------
        phase_name: str
            the phase_name of the UpdateKillChainPhase

        Returns:
        --------
        UpdateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.phase_name = phase_name
        return self

    def with_stix_representation(self, stix_representation: dict):
        """This function fill the stix representation in the contract

        Parameters:
        -----------
        stix_representation: dict
            the stix representation of the CreateKillChainPhase

        Returns:
        --------
        CreateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.stix_representation = stix_representation
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        UpdateKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> UpdateKillChainPhaseOutputPort:
        """This function return the filled contract

        Returns:
        --------
        UpdateKillChainPhaseOutputPort
            the contract filled

        """

        return self.__output
