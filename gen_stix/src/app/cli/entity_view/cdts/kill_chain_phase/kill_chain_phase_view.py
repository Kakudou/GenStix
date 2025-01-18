"""This module is the KillChainPhase that will be shown"""

from dataclasses import dataclass
from json import dumps as json_dumps


@dataclass
class KillChainPhaseView:
    """This class defined the attributes that we want to show

    Attributes:
    -----------
    __kill_chain_name: str
        The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    __phase_name: str
        The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    __stix_representation: str
        The json representation of the kill chain phase

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __kill_chain_name: str = None
    __phase_name: str = None
    __stix_representation: str = None

    @property
    def kill_chain_name(self) -> str:
        return self.__kill_chain_name

    @kill_chain_name.setter
    def kill_chain_name(self, kill_chain_name: str):
        self.__kill_chain_name = kill_chain_name

    @property
    def phase_name(self) -> str:
        return self.__phase_name

    @phase_name.setter
    def phase_name(self, phase_name: str):
        self.__phase_name = phase_name

    @property
    def stix_representation(self) -> str:
        return self.__stix_representation

    @stix_representation.setter
    def stix_representation(self, stix_representation: str):
        self.__stix_representation = stix_representation

    @staticmethod
    def from_contract(contract):
        kill_chain_phase = KillChainPhaseView()
        kill_chain_phase.kill_chain_name = contract.kill_chain_name
        kill_chain_phase.phase_name = contract.phase_name
        kill_chain_phase.stix_representation = json_dumps(
            contract.stix_representation, indent=2
        )

        return kill_chain_phase
