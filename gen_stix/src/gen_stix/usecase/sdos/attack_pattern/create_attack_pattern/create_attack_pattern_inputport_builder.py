"""This module is the builder that ensure the filling of the input contract"""

from dataclasses import dataclass
from typing import Any, List, Dict
from gen_stix.src.gen_stix.usecase.sdos.attack_pattern.create_attack_pattern.create_attack_pattern_inputport import (
    CreateAttackPatternInputPort,
)


@dataclass
class CreateAttackPatternInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: CreateAttackPatternInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_type_: str
        fill the type_ in the contract
    with_external_references: List
        fill the external_references in the contract
    with_name: str
        fill the name in the contract
    with_description: str
        fill the description in the contract
    with_aliases: List[str]
        fill the aliases in the contract
    with_kill_chain_phases: List
        fill the kill_chain_phases in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """This function create the empty contract

        Returns:
        --------
        CreateAttackPatternInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = CreateAttackPatternInputPort()
        return self

    def with_type_(self, type_: str):
        """This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_type_(type_)
        self.__input.type_ = type_
        return self

    def _validate_type_(self, type_: str):
        """This function check the  validity of type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the CreateAttackPattern

        Returns:
        --------

        """

        if type_ is None or type == "":
            raise ValueError("`type` is a required field for AttackPattern")
        elif type_ != "attack-pattern":
            raise ValueError("`type` must be `attack-pattern`.")

    def with_external_references(self, external_references: List):
        """This function fill the external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_external_references(external_references)
        self.__input.external_references = external_references
        return self

    def _validate_external_references(self, external_references: List):
        """This function check the  validity of external_references in the contract

        Parameters:
        -----------
        external_references: List
            the external_references of the CreateAttackPattern

        Returns:
        --------

        """

        if external_references is not None:
            if not isinstance(external_references, List):
                raise ValueError(
                    "`external_references` must be a List[external-reference]."
                )
            else:
                for external_ref in external_references:
                    if not isinstance(external_ref, Dict):
                        raise ValueError(
                            "`external_references` must be a List[external-reference]."
                        )
                    elif external_ref["source_name"] is None:
                        raise ValueError(
                            "`external_references` must be a List[external-reference]."
                        )
                    elif (
                        external_ref["source_name"] == "capec"
                        and external_ref["external_id"] is None
                    ):
                        raise ValueError(
                            "`external_references` must be a List[external-reference]."
                        )
                    elif external_ref[
                        "source_name"
                    ] == "capec" and not external_ref[
                        "external_id"
                    ].startswith(
                        "CAPEC-"
                    ):
                        raise ValueError(
                            "`external_references` must be a List[external-reference]."
                        )
                    elif external_ref["source_name"] == "":
                        raise ValueError(
                            "`external_references` must be a List[external-reference]."
                        )

    def with_name(self, name: str):
        """This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_name(name)
        self.__input.name = name
        return self

    def _validate_name(self, name: str):
        """This function check the  validity of name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateAttackPattern

        Returns:
        --------

        """

        if name is None or name == "":
            raise ValueError("`name` is a required field for AttackPattern")
        elif type(name) is not str:
            raise ValueError("`name` must be a str.")

    def with_description(self, description: str):
        """This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_description(description)
        self.__input.description = description
        return self

    def _validate_description(self, description: str):
        """This function check the  validity of description in the contract

        Parameters:
        -----------
        description: str
            the description of the CreateAttackPattern

        Returns:
        --------

        """

        if description is not None:
            if type(description) is not str:
                raise ValueError("`description` must be a str.")

    def with_aliases(self, aliases: List[str]):
        """This function fill the aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_aliases(aliases)
        self.__input.aliases = aliases
        return self

    def _validate_aliases(self, aliases: List[str]):
        """This function check the  validity of aliases in the contract

        Parameters:
        -----------
        aliases: List[str]
            the aliases of the CreateAttackPattern

        Returns:
        --------

        """

        if aliases is not None:
            if not isinstance(aliases, List):
                raise ValueError("`aliases` must be a List[str].")
            elif not all(isinstance(alias, str) for alias in aliases):
                raise ValueError("`aliases` must be a List[str].")

    def with_kill_chain_phases(self, kill_chain_phases: List):
        """This function fill the kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------
        CreateAttackPatternOutputPortBuilder
            this builder with the contract to fill

        """

        self._validate_kill_chain_phases(kill_chain_phases)
        self.__input.kill_chain_phases = kill_chain_phases
        return self

    def _validate_kill_chain_phases(self, kill_chain_phases: List):
        """This function check the  validity of kill_chain_phases in the contract

        Parameters:
        -----------
        kill_chain_phases: List
            the kill_chain_phases of the CreateAttackPattern

        Returns:
        --------

        """

        if kill_chain_phases is not None:
            if not isinstance(kill_chain_phases, List):
                raise ValueError(
                    "`kill_chain_phases` must be a List[kill-chain-phase]."
                )
            elif not all(
                isinstance(kill_chain_phase, Dict)
                for kill_chain_phase in kill_chain_phases
            ):
                raise ValueError(
                    "`kill_chain_phases` must be a List[kill-chain-phase]."
                )

    def build(self) -> CreateAttackPatternInputPort:
        """This function return the filled contract

        Returns:
        --------
        CreateAttackPatternInputPort
            the contract filled

        """

        self._validate_type_(self.__input.type_)
        self._validate_external_references(self.__input.external_references)
        self._validate_name(self.__input.name)
        self._validate_description(self.__input.description)
        self._validate_aliases(self.__input.aliases)
        self._validate_kill_chain_phases(self.__input.kill_chain_phases)

        return self.__input
