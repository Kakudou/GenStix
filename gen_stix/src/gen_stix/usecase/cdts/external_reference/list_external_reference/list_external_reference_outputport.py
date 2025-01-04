""""This module define the output contract to create a ListExternalReference"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListExternalReferenceOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_external_references: List[str]
        List of all external_references

    """

    error: str = None
    all_external_references: List[str] = None
