"""This module is the ExternalReference that will be shown"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ExternalReferenceView:
    """This class defined the attributes that we want to show

    Attributes:
    -----------
    __source_name: str
        The name of the source that the external-reference is defined within (system, registry, organization, etc.).
    __description: str
        A human readable description.
    __url: str
        A URL reference to an external resource [RFC3986].
    __hashes: Dict
        Specifies a dictionary of hashes for the contents of the url. This SHOULD be provided when the url property is present. Dictionary keys MUST come from one of the entries listed in the hash-algorithm-ov open vocabulary. As stated in Section 2.7, to ensure interoperability, a SHA-256 hash SHOULD be included whenever possible.
    __external_id: str
        An identifier for the external reference content.

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __source_name: str = None
    __description: str = None
    __url: str = None
    __hashes: Dict = None
    __external_id: str = None

    @property
    def source_name(self) -> str:
        return self.__source_name

    @source_name.setter
    def source_name(self, source_name: str):
        self.__source_name = source_name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def hashes(self) -> Dict:
        return self.__hashes

    @hashes.setter
    def hashes(self, hashes: Dict):
        self.__hashes = hashes

    @property
    def external_id(self) -> str:
        return self.__external_id

    @external_id.setter
    def external_id(self, external_id: str):
        self.__external_id = external_id

    @staticmethod
    def from_contract(contract):
        external_reference = ExternalReferenceView()
        external_reference.source_name = contract.source_name
        external_reference.description = contract.description
        external_reference.url = contract.url
        external_reference.hashes = contract.hashes
        external_reference.external_id = contract.external_id

        return external_reference
