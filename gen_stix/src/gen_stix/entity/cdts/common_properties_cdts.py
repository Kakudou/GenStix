"""This module will handle the common properties of the CDTs."""


class CommonPropertiesCDTs:
    """This class will handle the common properties of the CDTs.

    Attributes:
    -----------
    Core properties
        __stix_representation: dict
            The json that will represent the object in the STIX format

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __stix_representation: dict = None

    @property
    def stix_representation(self) -> dict:
        """Get the stix representation."""
        return self.__stix_representation

    @stix_representation.setter
    def stix_representation(self, stix_representation: dict) -> None:
        """Set the stix representation."""
        self.__stix_representation = stix_representation
