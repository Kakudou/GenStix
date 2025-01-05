""" This module use the usecase ReadKillChainPhase"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.read_kill_chain_phase.read_kill_chain_phase_inputport_builder import (
    ReadKillChainPhaseInputPortBuilder,
)


class ReadKillChainPhaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadKillChainPhase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadKillChainPhaseInputPort
        with the use of ReadKillChainPhaseInputPortBuilder.
        Then this contract will be gave to ReadKillChainPhase usecase.
        In return we should obtain the contract ReadKillChainPhaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            kill_chain_name: str
                The name of the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.
            phase_name: str
                The name of the phase in the kill chain. The value of this property SHOULD be all lowercase and SHOULD use hyphens instead of spaces or underscores as word separators.

        Returns:
        --------
        ReadKillChainPhase_oc
            the output contract of the usecase ReadKillChainPhase

        """

        sanitize_kill_chain_name = inputs["kill_chain_name"]
        sanitize_phase_name = inputs["phase_name"]

        read_kill_chain_phase_icb = ReadKillChainPhaseInputPortBuilder()
        read_kill_chain_phase_ic = (
            read_kill_chain_phase_icb.create()
            .with_kill_chain_name(sanitize_kill_chain_name)
            .with_phase_name(sanitize_phase_name)
            .build()
        )

        read_kill_chain_phase_oc = Container.get_usecase_repo(
            "ReadKillChainPhase", storage_engine
        ).execute(read_kill_chain_phase_ic)

        return read_kill_chain_phase_oc
