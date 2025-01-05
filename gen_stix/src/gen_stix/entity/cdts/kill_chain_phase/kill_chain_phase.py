"""This module is the core defined entity for KillChainPhase"""

from dataclasses import dataclass


@dataclass
class KillChainPhase:
    """This class defined the attributes for KillChainPhase

    Attributes:
    -----------
    __kill_chain_name: str
        The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    __phase_name: str
        The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __kill_chain_name: str = None
    __phase_name: str = None

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
