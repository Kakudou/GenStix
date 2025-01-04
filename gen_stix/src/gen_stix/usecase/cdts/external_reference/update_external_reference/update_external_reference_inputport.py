""""This module define the input contract to create a UpdateExternalReference"""
from dataclasses\
    import dataclass
from typing\
    import Dict


@dataclass
class UpdateExternalReferenceInputPort:
    """"This class define the necessary attributes to create a ExternalReference

    Attributes:
    -----------
    source_name: str
        The name of the source that the external-reference is defined within (system, registry, organization, etc.).
    description: str
        A human readable description.
    url: str
        A URL reference to an external resource [RFC3986].
    hashes: Dict
        Specifies a dictionary of hashes for the contents of the url. This SHOULD be provided when the url property is present. Dictionary keys MUST come from one of the entries listed in the hash-algorithm-ov open vocabulary. As stated in Section 2.7, to ensure interoperability, a SHA-256 hash SHOULD be included whenever possible.
    external_id: str
        An identifier for the external reference content.

    """

    source_name: str = None
    description: str = None
    url: str = None
    hashes: Dict = None
    external_id: str = None
