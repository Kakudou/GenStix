""""This module define the output contract to create a UpdateAttackPattern"""

from dataclasses import dataclass
from typing import List


@dataclass
class UpdateAttackPatternOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    type_: str
        The value of this property **MUST** be attack-pattern.
    external_references: List
        A list of external references which refer to non-STIX information. This property MAY be used to provide one or more Attack Pattern identifiers, such as a CAPEC ID. When specifying a CAPEC ID, the source_name property of the external reference MUST be set to capec and the external_id property MUST be formatted as CAPEC-[id].
    name: str
        A name used to identify the Attack Pattern.
    description: str
        A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.
    aliases: List[str]
        Alternative names used to identify this Attack Pattern.
    kill_chain_phases: List
        The list of Kill Chain Phases for which this Attack Pattern is used.

    """

    error: str = None
    type_: str = None
    external_references: List = None
    name: str = None
    description: str = None
    aliases: List[str] = None
    kill_chain_phases: List = None
