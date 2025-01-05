"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_inputport import (
    ListKillChainPhaseInputPort,
)


@dataclass
class ListKillChainPhaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListKillChainPhaseInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        ListKillChainPhaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListKillChainPhaseInputPort()
        return self

    def build(self) -> ListKillChainPhaseInputPort:
        """This function return the filled contract

        Returns:
        --------
        ListKillChainPhaseInputPort
            the contract filled

        """

        return self.__input
