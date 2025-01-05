""""This module define the input contract to create a ReadAttackPattern"""

from dataclasses import dataclass


@dataclass
class ReadAttackPatternInputPort:
    """ "This class define the necessary attributes to create a AttackPattern

    Attributes:
    -----------
    type_: str
        The value of this property **MUST** be attack-pattern.
    name: str
        A name used to identify the Attack Pattern.

    """

    type_: str = None
    name: str = None
