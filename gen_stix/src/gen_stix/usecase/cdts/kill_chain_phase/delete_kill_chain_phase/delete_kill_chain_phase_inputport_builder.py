"""This module is the builder that ensure the filling of the input contract"""

import re

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_inputport import (
    DeleteKillChainPhaseInputPort,
)


@dataclass
class DeleteKillChainPhaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: DeleteKillChainPhaseInputPort
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
        DeleteKillChainPhaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = DeleteKillChainPhaseInputPort()
        return self

    def with_kill_chain_name(self, kill_chain_name: str):
        """This function fill the kill_chain_name in the contract

        Parameters:
        -----------
        kill_chain_name: str
            the kill_chain_name of the DeleteKillChainPhase

        Returns:
        --------
        DeleteKillChainPhaseOutputPortBuilder
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
            the kill_chain_name of the DeleteKillChainPhase

        Returns:
        --------

        """

        if kill_chain_name is None or kill_chain_name == "":
            raise ValueError(
                "`kill_chain_name` is a required field for KillChainPhase"
            )
        elif type(kill_chain_name) is not str:
            raise ValueError(
                "`kill_chain_name` must be a str in lowercase with hyphens."
            )
        elif type(kill_chain_name) is str:
            pattern = r"^[0-9a-z-]?$"
            if bool(re.match(pattern, kill_chain_name)):
                raise ValueError(
                    "`kill_chain_name` must be a str in lowercase with hyphens."
                )

    def with_phase_name(self, phase_name: str):
        """This function fill the phase_name in the contract

        Parameters:
        -----------
        phase_name: str
            the phase_name of the DeleteKillChainPhase

        Returns:
        --------
        DeleteKillChainPhaseOutputPortBuilder
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
            the phase_name of the DeleteKillChainPhase

        Returns:
        --------

        """

        if phase_name is None or phase_name == "":
            raise ValueError(
                "`phase_name` is a required field for KillChainPhase"
            )
        elif type(phase_name) is not str:
            raise ValueError(
                "`phase_name` must be a str in lowercase with hyphens."
            )
        elif type(phase_name) is str:
            pattern = r"^[0-9a-z-]?$"
            if bool(re.match(pattern, phase_name)):
                raise ValueError(
                    "`phase_name` must be a str in lowercase with hyphens."
                )

    def build(self) -> DeleteKillChainPhaseInputPort:
        """This function return the filled contract

        Returns:
        --------
        DeleteKillChainPhaseInputPort
            the contract filled

        """

        self._validate_kill_chain_name(self.__input.kill_chain_name)
        self._validate_phase_name(self.__input.phase_name)

        return self.__input
