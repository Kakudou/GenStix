""""This module define the input contract to create a ReadKillChainPhase"""

from dataclasses import dataclass


@dataclass
class ReadKillChainPhaseInputPort:
    """ "This class define the necessary attributes to create a KillChainPhase

    Attributes:
    -----------
    kill_chain_name: str
        The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
    phase_name: str
        The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

    """

    kill_chain_name: str = None
    phase_name: str = None
