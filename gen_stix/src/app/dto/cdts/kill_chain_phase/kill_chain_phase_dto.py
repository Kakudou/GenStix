"""This module is the KillChainPhaseDTO that will be persist"""

from json import loads as json_loads
from dataclasses import dataclass
from stix2 import KillChainPhase


@dataclass
class KillChainPhaseDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of KillChainPhase: (kill_chain_name, phase_name)
    __kill_chain_name: str
        The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    __phase_name: str
        The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __id: str = None
    __kill_chain_name: str = None
    __phase_name: str = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

    def to_stix21(self) -> str:
        """
        This method will convert the DTO to KillChainPhase object

        Returns:
        --------
        KillChainPhase
            The KillChainPhase object
        """
        kill_chain_phase = KillChainPhase(
            kill_chain_name=self.kill_chain_name, phase_name=self.phase_name
        )

        return kill_chain_phase.serialize(pretty=True, indent=2)

    def from_stix21(self, kill_chain_phase: str):
        """
        This method will convert the KillChainPhase object to DTO

        Parameters:
        -----------
        kill_chain_phase: KillChainPhase
            The KillChainPhase object
        """

        kill_chain_stix21 = KillChainPhase(**json_loads(kill_chain_phase))

        self.kill_chain_name = kill_chain_stix21.kill_chain_name
        self.phase_name = kill_chain_stix21.phase_name
