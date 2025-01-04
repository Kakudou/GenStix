""""This module define the output contract to create a DeleteExternalReference"""
from dataclasses\
    import dataclass


@dataclass
class DeleteExternalReferenceOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    deleted: bool
        Flag true if deleted

    """

    error: str = None
    deleted: bool = None
