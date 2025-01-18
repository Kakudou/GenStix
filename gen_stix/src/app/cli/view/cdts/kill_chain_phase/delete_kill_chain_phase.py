"""This module handle the form and delete a kill chain phase"""

from gen_stix.src.app.adapter.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_adapter import (
    DeleteKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_adapter import (
    ListKillChainPhaseAdapter,
)

from gen_stix.src import STORAGE_ENGINE
from gen_stix.src.app.repository.infile.infile_persist import InFilePersist
from gen_stix.src.app.cli.view.project.read_project import ReadProject
from gen_stix.src.app.cli.view.factory import Factory


class DeleteKillChainPhase:

    @staticmethod
    def show(
        project_name=None,
        projects_path=None,
        kill_chain_name=None,
        phase_name=None,
    ):

        if project_name is not None:
            print(f"Deleting a kill chain phase for project {project_name}")
            ifr = InFilePersist()
            if projects_path is not None:
                ifr.save_path = f"{projects_path}/{project_name}"
            else:
                ifr.save_path = f"{ifr.save_path}/{project_name}"
        else:
            print("You must select a project first")
            ReadProject.show(
                project_dir=projects_path, referer="Delete 'Kill Chain Phase'"
            )

        inputs = {}
        if kill_chain_name is None and phase_name is None:
            list_kill_chain_phase_contract = (
                ListKillChainPhaseAdapter().execute({})
            )

            if list_kill_chain_phase_contract.error is not None:
                print(f"Error: {list_kill_chain_phase_contract.error}")
                exit(1)
            if list_kill_chain_phase_contract.all_kill_chain_phases == []:
                print("There are no kill chain phases in the system.")
                exit(0)

            list_kill_chain_phase = (
                list_kill_chain_phase_contract.all_kill_chain_phases
            )
            kill_chain_phase = Factory.paginated_list_factory(
                list_kill_chain_phase, "The Kill Chain Phases"
            )
            inputs = {
                "kill_chain_name": kill_chain_phase.split(" - ")[0],
                "phase_name": kill_chain_phase.split(" - ")[1],
            }
        else:
            inputs = {
                "kill_chain_name": kill_chain_name,
                "phase_name": phase_name,
            }

        print("\r\nDeleting kill chain phase...")
        kill_chain_phase = DeleteKillChainPhaseAdapter().execute(
            inputs, STORAGE_ENGINE
        )

        if kill_chain_phase.error is not None:
            print(f"Error: {kill_chain_phase.error}")
            exit(1)

        if kill_chain_phase.deleted:
            print("Kill chain phase deleted successfully.")
