"""This module will handle the common properties of the SDOs."""


class CommonPropertiesSDOs:
    """This class will handle the common properties of the SDOs.
    Those attributes are use in stix SDOS, but are not required in th core engine of that application.
    For that reason, we have created a separate class to handle those.

    Attributes:
    -----------
    Required properties:
        __spec_version: str
            The version of the STIX specification used to represent this object.
            The value of this property MUST be 2.1 for STIX Objects defined according to this specification.
            If objects are found where this property is not present, the implicit value for all STIX Objects other than SCOs is 2.0. Since SCOs are now top-level objects in STIX 2.1, the default value for SCOs is 2.1.
        __id: str
            The id property uniquely identifies this object.
            For objects that support versioning, all objects with the same id are considered different versions of the same object and the version of the object is identified by its modified property.
        __created: str
            The created property represents the time at which the object was originally created.
            The object creator can use the time it deems most appropriate as the time the object was created. The minimum precision MUST be milliseconds (three digits after the decimal place in seconds), but MAY be more precise.
            The created property MUST NOT be changed when creating a new version of the object.
            See section 3.6 for further definition of versioning.
        __modified: str
            The modified property is only used by STIX Objects that support versioning and represents the time that this particular version of the object was last modified.
            The object creator can use the time it deems most appropriate as the time this version of the object was modified. The minimum precision MUST be milliseconds (three digits after the decimal place in seconds), but MAY be more precise.
            If the created property is defined, then the value of the modified property for a given object version MUST be later than or equal to the value of the created property.
            Object creators MUST set the modified property when creating a new version of an object if the created property was set.
            See section 3.6 for further definition of versioning.

    Optional properties
        __created_by_ref: str
            The created_by_ref property specifies the id property of the identity object that describes the entity that created this object.
            If this attribute is omitted, the source of this information is undefined. This may be used by object creators who wish to remain anonymous.
        __revoked: bool
            The modified property is only used by STIX Objects that support versioning and represents the time that this particular version of the object was last modified.
            The object creator can use the time it deems most appropriate as the time this version of the object was modified. The minimum precision MUST be milliseconds (three digits after the decimal place in seconds), but MAY be more precise.
            If the created property is defined, then the value of the modified property for a given object version MUST be later than or equal to the value of the created property.
            Object creators MUST set the modified property when creating a new version of an object if the created property was set.
            See section 3.6 for further definition of versioning.
        __labels: list
            The labels property specifies a set of terms used to describe this object. The terms are user-defined or trust-group defined and their meaning is outside the scope of this specification and MAY be ignored.
            Where an object has a specific property defined in the specification for characterizing subtypes of that object, the labels property MUST NOT be used for that purpose.
            For example, the Malware SDO has a property malware_types that contains a list of Malware subtypes (dropper, RAT, etc.). In this example, the labels property cannot be used to describe these Malware subtypes.
        __confidence: int
            The confidence property identifies the confidence that the creator has in the correctness of their data. The confidence value MUST be a number in the range of 0-100.
            Appendix A contains a table of normative mappings to other confidence scales that MUST be used when presenting the confidence value in one of those scales.
            If the confidence property is not present, then the confidence of the content is unspecified.
        __lang: str
            The lang property identifies the language of the text content in this object. When present, it MUST be a language code conformant to [RFC5646]. If the property is not present, then the language of the content is en (English).
            This property SHOULD be present if the object type contains translatable text properties (e.g. name, description).
            The language of individual fields in this object MAY be overridden by the lang property in granular markings (see section 7.2.3).
        __external_references: list
            The external_references property specifies a list of external references which refers to non-STIX information. This property is used to provide one or more URLs, descriptions, or IDs to records in other systems.
        __object_marking_refs: list
            The object_marking_refs property specifies a list of id properties of marking-definition objects that apply to this object.
            In some cases, though uncommon, marking definitions themselves may be marked with sharing or handling guidance. In this case, this property MUST NOT contain any references to the same Marking Definition object (i.e., it cannot contain any circular references).
            See section 7.2 for further definition of data markings.
        __granular_markings: list
            The granular_markings property specifies a list of granular markings applied to this object.
            In some cases, though uncommon, marking definitions themselves may be marked with sharing or handling guidance. In this case, this property MUST NOT contain any references to the same Marking Definition object (i.e., it cannot contain any circular references).
            See section 7.2 for further definition of data markings.
        __extensions: dict
            Specifies any extensions of the object, as a dictionary.
            Dictionary keys SHOULD be the id of a STIX Extension object or the name of a predefined object extension found in this specification, depending on the type of extension being used.
            The corresponding dictionary values MUST contain the contents of the extension instance.
            Each extension dictionary MAY contain the property extension_type. The value of this property MUST come from the extension-type-enum enumeration. If the extension_type property is not present, then this is a predefined extension which does not use the extension facility described in section 7.3. When this extension facility is used the extension_type property MUST be present.

    Core properties
        __stix_representation: dict
            The json that will represent the object in the STIX format

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __spec_version: str = "2.1"
    __id: str = None
    __created: str = None
    __modified: str = None

    __created_by_ref: str = None
    __revoked: bool = None
    __labels: list = None
    __confidence: int = None
    __lang: str = None
    __external_references: list = None
    __object_marking_refs: list = None
    __granular_markings: list = None
    __extensions: dict = None

    __stix_representation: dict = None

    @property
    def spec_version(self) -> str:
        return self.__spec_version

    @spec_version.setter
    def spec_version(self, spec_version: str):
        self.__spec_version = spec_version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id_: str):
        self.__id = id_

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def modified(self) -> str:
        return self.__modified

    @modified.setter
    def modified(self, modified: str):
        self.__modified = modified

    @property
    def created_by_ref(self) -> str:
        return self.__created_by_ref

    @created_by_ref.setter
    def created_by_ref(self, created_by_ref: str):
        self.__created_by_ref = created_by_ref

    @property
    def revoked(self) -> bool:
        return self.__revoked

    @revoked.setter
    def revoked(self, revoked: bool):
        self.__revoked = revoked

    @property
    def labels(self) -> list:
        return self.__labels

    @labels.setter
    def labels(self, labels: list):
        self.__labels = labels

    @property
    def confidence(self) -> int:
        return self.__confidence

    @confidence.setter
    def confidence(self, confidence: int):
        self.__confidence = confidence

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def external_references(self) -> list:
        return self.__external_references

    @external_references.setter
    def external_references(self, external_references: list):
        self.__external_references = external_references

    @property
    def object_marking_refs(self) -> list:
        return self.__object_marking_refs

    @object_marking_refs.setter
    def object_marking_refs(self, object_marking_refs: list):
        self.__object_marking_refs = object_marking_refs

    @property
    def granular_markings(self) -> list:
        return self.__granular_markings

    @granular_markings.setter
    def granular_markings(self, granular_markings: list):
        self.__granular_markings = granular_markings

    @property
    def extensions(self) -> dict:
        return self.__extensions

    @extensions.setter
    def extensions(self, extensions: dict):
        self.__extensions = extensions

    @property
    def stix_representation(self) -> dict:
        return self.__stix_representation

    @stix_representation.setter
    def stix_representation(self, stix_representation: dict):
        self.__stix_representation = stix_representation
