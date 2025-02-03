"""This module is the ExternalReferenceDTO that will be persist"""

from json import loads as json_loads
from dataclasses import dataclass
from typing import Dict
from stix2 import ExternalReference


@dataclass
class ExternalReferenceDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of ExternalReference: (source_name, external_id)
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

    __id: str = None
    __source_name: str = None
    __description: str = None
    __url: str = None
    __hashes: Dict = None
    __external_id: str = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

    def to_stix21(self) -> dict:
        """
        This method will convert the DTO to ExternalReference object

        Returns:
        --------
        ExternalReference
            The ExternalReference object
        """
        external_reference = ExternalReference(
            source_name=self.source_name,
            external_id=self.external_id,
            description=self.description,
            url=self.url,
            hashes=self.hashes,
        )

        return json_loads(external_reference.serialize())

    def from_stix21(self, external_reference: str):
        """
        This method will convert the ExternalReference object to DTO

        Parameters:
        -----------
        external_reference: ExternalReference
            The ExternalReference object
        """

        external_reference_stix21 = ExternalReference(
            **json_loads(external_reference)
        )

        self.source_name = external_reference_stix21.source_name
        self.external_id = external_reference_stix21.external_id
        if "description" in external_reference_stix21.keys():
            self.description = external_reference_stix21.description
        if "url" in external_reference_stix21.keys():
            self.url = external_reference_stix21.url
        if "hashes" in external_reference_stix21.keys():
            self.hashes = external_reference_stix21.hashes
