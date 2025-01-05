""""This module define the output contract to create a ListKillChainPhase"""

from dataclasses import dataclass
from typing import List


@dataclass
class ListKillChainPhaseOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_kill_chain_phases: List[str]
        List of all kill_chain_phases

    """

    error: str = None
    all_kill_chain_phases: List[str] = None
