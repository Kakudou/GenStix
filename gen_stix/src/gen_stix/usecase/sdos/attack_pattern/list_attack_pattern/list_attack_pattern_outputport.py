""""This module define the output contract to create a ListAttackPattern"""

from dataclasses import dataclass
from typing import List


@dataclass
class ListAttackPatternOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_attack_patterns: List[str]
        List of all attack_patterns

    """

    error: str = None
    all_attack_patterns: List[str] = None
