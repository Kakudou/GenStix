""""This module define the input contract to create a DeleteExternalReference"""

from dataclasses import dataclass


@dataclass
class DeleteExternalReferenceInputPort:
    """ "This class define the necessary attributes to create a ExternalReference

    Attributes:
    -----------
    source_name: str
        The name of the source that the external-reference is defined within (system, registry, organization, etc.).
    external_id: str
        An identifier for the external reference content.

    """

    source_name: str = None
    external_id: str = None
