"""This module is the builder that ensure the filling of the output contract"""

from dataclasses import dataclass
from typing import Any, List
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_outputport import (
    ListKillChainPhaseOutputPort,
)


@dataclass
class ListKillChainPhaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListKillChainPhaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_kill_chain_phases: List[str]
        fill the all_kill_chain_phases in the contract
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
        ListKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListKillChainPhaseOutputPort()
        return self

    def with_all_kill_chain_phases(self, all_kill_chain_phases: List[str]):
        """This function fill the all_kill_chain_phases in the contract

        Parameters:
        -----------
        all_kill_chain_phases: List[str]
            the all_kill_chain_phases of the ListKillChainPhase

        Returns:
        --------
        ListKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_kill_chain_phases = all_kill_chain_phases
        return self

    def with_error(self, error: str):
        """This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListKillChainPhaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListKillChainPhaseOutputPort:
        """This function return the filled contract

        Returns:
        --------
        ListKillChainPhaseOutputPort
            the contract filled

        """

        return self.__output
