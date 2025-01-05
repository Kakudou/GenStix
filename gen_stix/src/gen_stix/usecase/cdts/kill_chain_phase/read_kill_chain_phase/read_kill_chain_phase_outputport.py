""""This module define the output contract to create a ReadKillChainPhase"""

from dataclasses import dataclass


@dataclass
class ReadKillChainPhaseOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    kill_chain_name: str
        The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    phase_name: str
        The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

    """

    error: str = None
    kill_chain_name: str = None
    phase_name: str = None
