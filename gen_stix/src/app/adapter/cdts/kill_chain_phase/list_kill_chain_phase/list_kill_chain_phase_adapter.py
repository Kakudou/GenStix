""" This module use the usecase ListKillChainPhase"""

from typing import Dict

from gen_stix.src import STORAGE_ENGINE

from gen_stix.src.utils.container import Container
from gen_stix.src.gen_stix.usecase.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_inputport_builder import (
    ListKillChainPhaseInputPortBuilder,
)


class ListKillChainPhaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListKillChainPhase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListKillChainPhaseInputPort
        with the use of ListKillChainPhaseInputPortBuilder.
        Then this contract will be gave to ListKillChainPhase usecase.
        In return we should obtain the contract ListKillChainPhaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListKillChainPhase_oc
            the output contract of the usecase ListKillChainPhase

        """

        list_kill_chain_phase_icb = ListKillChainPhaseInputPortBuilder()
        list_kill_chain_phase_ic = list_kill_chain_phase_icb.create().build()

        list_kill_chain_phase_oc = Container.get_usecase_repo(
            "ListKillChainPhase", storage_engine
        ).execute(list_kill_chain_phase_ic)

        return list_kill_chain_phase_oc
