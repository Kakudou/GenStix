"""This module is the AttackPatternDTO that will be persist"""

from dataclasses import dataclass
from typing import List


@dataclass
class AttackPatternDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of AttackPattern: (type_, name)
    __type_: str
        The value of this property **MUST** be attack-pattern.
    __external_references: List
        A list of external references which refer to non-STIX information. This property MAY be used to provide one or more Attack Pattern identifiers, such as a CAPEC ID. When specifying a CAPEC ID, the source_name property of the external reference MUST be set to capec and the external_id property MUST be formatted as CAPEC-[id].
    __name: str
        A name used to identify the Attack Pattern.
    __description: str
        A description that provides more details and context about the Attack Pattern, potentially including its purpose and its key characteristics.
    __aliases: List[str]
        Alternative names used to identify this Attack Pattern.
    __kill_chain_phases: List
        The list of Kill Chain Phases for which this Attack Pattern is used.

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __id: str = None
    __type_: str = None
    __external_references: List = None
    __name: str = None
    __description: str = None
    __aliases: List[str] = None
    __kill_chain_phases: List = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type_(self) -> str:
        return self.__type_

    @type_.setter
    def type_(self, type_: str):
        self.__type_ = type_

    @property
    def external_references(self) -> List:
        return self.__external_references

    @external_references.setter
    def external_references(self, external_references: List):
        self.__external_references = external_references

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aliases(self) -> List[str]:
        return self.__aliases

    @aliases.setter
    def aliases(self, aliases: List[str]):
        self.__aliases = aliases

    @property
    def kill_chain_phases(self) -> List:
        return self.__kill_chain_phases

    @kill_chain_phases.setter
    def kill_chain_phases(self, kill_chain_phases: List):
        self.__kill_chain_phases = kill_chain_phases
