"""This enum will contains all the hashes OpenVocabulary"""

from enum import Enum


class HashesOV(Enum):
    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"
    SHA3_256 = "SHA3-256"
    SHA3_512 = "SHA3-512"
    SSDEEP = "SSDEEP"
    TLSH = "TLSH"

    @classmethod
    def from_value(cls, value):
        if not hasattr(cls, f"_{cls.__name__}__value_to_key"):
            cls.__value_to_key = {v.value: v for v in cls}
        key = cls.__value_to_key.get(value)
        if key is None:
            raise ValueError(f"No hashes-ov found for {value}.")
        return key
