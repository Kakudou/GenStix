"""This module handle the form and access a kill chain phase from it"""

from gen_stix.src.app.adapter.cdts.kill_chain_phase.read_kill_chain_phase.read_kill_chain_phase_adapter import (
    ReadKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_adapter import (
    ListKillChainPhaseAdapter,
)
from gen_stix.src.app.cli.entity_view.cdts.kill_chain_phase.kill_chain_phase_view import (
    KillChainPhaseView,
)

import questionary
from gen_stix.src.app.cli.view.main_menu import MainMenu
from gen_stix.src import STORAGE_ENGINE
from gen_stix.src.app.repository.infile.infile_persist import InFilePersist
from gen_stix.src.app.cli.view.project.read_project import ReadProject
from gen_stix.src.app.cli.view.factory import Factory


class ReadKillChainPhase:

    @staticmethod
    def show(
        project_name=None,
        projects_path=None,
        kill_chain_name=None,
        phase_name=None,
    ):

        if project_name is not None:
            print(f"Accessing a kill chain phase for project {project_name}")
            ifr = InFilePersist()
            if projects_path is not None:
                ifr.save_path = f"{projects_path}/{project_name}"
            else:
                ifr.save_path = f"{ifr.save_path}/{project_name}"
        else:
            print("You must select a project first")
            ReadProject.show(
                project_dir=projects_path, referer="Read 'Kill Chain Phase'"
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

        print("\r\nAccessing kill chain phase...")
        kill_chain_phase = ReadKillChainPhaseAdapter().execute(
            inputs, STORAGE_ENGINE
        )

        if kill_chain_phase.error is not None:
            print(f"Error: {kill_chain_phase.error}")
            exit(1)

        kc_view = KillChainPhaseView.from_contract(kill_chain_phase)
        print("\r\nKill Chain Phase successfully retrieved.")
        print("\r\nThe kill chain phase has the following attributes:")
        print(f"Kill Chain Name: {kc_view.kill_chain_name}")
        print(f"Phase Name: {kc_view.phase_name}")
        print("\r\nThe json representation of the kill chain phase is:")
        print(kc_view.stix_representation)

        print("\r\n\r\nWhat do you want to do next?")
        action = questionary.select(
            "Select an action:",
            choices=[
                "Manage kill chain phase",
                "Return to the main menu",
                "Exit",
            ],
            use_shortcuts=True,
            use_arrow_keys=True,
        ).ask()

        if action == "Manage kill chain phase":
            MainMenu.show(
                project_name=project_name,
                projects_path=projects_path,
                type_stix="Kill Chain Phase",
            )
        elif action == "Return to the main menu":
            MainMenu.show(
                project_name=project_name, projects_path=projects_path
            )
        elif action == "Exit":
            exit(0)
