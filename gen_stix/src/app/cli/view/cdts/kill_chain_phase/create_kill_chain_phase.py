"""This module handle the form and create a kill chain phase from it"""

import questionary

from gen_stix.src.app.adapter.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_adapter import (
    CreateKillChainPhaseAdapter,
)
from gen_stix.src.app.cli.entity_view.cdts.kill_chain_phase.kill_chain_phase_view import (
    KillChainPhaseView,
)

from gen_stix.src import STORAGE_ENGINE
from gen_stix.src.app.cli.view.project.read_project import ReadProject
from gen_stix.src.app.cli.view.main_menu import MainMenu


class CreateKillChainPhase:

    @staticmethod
    def show(
        project_name=None,
        projects_path=None,
        kill_chain_name=None,
        phase_name=None,
    ):

        if project_name is None or projects_path is None:
            ReadProject.show(
                project_dir=projects_path,
                wanted_project=project_name,
                referer="Create 'Kill Chain Phase'",
            )

        if kill_chain_name is None and phase_name is None:

            answers = CreateKillChainPhase.create_kill_chain_phase_form()

            confirm = questionary.confirm(
                "Are you sure of the above inputs?", default=True
            ).ask()

            if not confirm:
                print("\r\n Ok, let's try again")
                CreateKillChainPhase.show()
            kill_chain_name = answers["kill_chain_name"]
            phase_name = answers["phase_name"]

        print("Creating kill chain phase...")
        name = f"{kill_chain_name}-{phase_name}"
        print(
            "The kill chain phase will be created with the following attributes:"
        )
        print(f"Name: {name}")
        print(f"Kill chain name: {kill_chain_name}")
        print(f"Phase name: {phase_name}")

        inputs = {}
        inputs["kill_chain_name"] = kill_chain_name
        inputs["phase_name"] = phase_name

        kill_chain = CreateKillChainPhaseAdapter.execute(
            inputs, STORAGE_ENGINE
        )

        if kill_chain.error is not None:
            print(f"Error: {kill_chain.error}")
            exit(1)

        print("Kill chain phase created successfully")
        kc_view = KillChainPhaseView.from_contract(kill_chain)

        print("The json representation of the kill chain phase is:")
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

    @staticmethod
    def create_kill_chain_phase_form():

        kill_chain_phase = {}

        kill_chain_phase["kill_chain_name"] = questionary.text(
            "What's the kill chain name?",
            validate=lambda val: (
                "The kill chain name must be in lowercase and contain only numbers, letters and hyphens"
                if len(val) == 0
                or not val.islower()
                or not val.replace("-", "").isalnum()
                else True
            ),
        ).ask()
        kill_chain_phase["phase_name"] = questionary.text(
            "What's the phase name?",
            validate=lambda val: (
                "The phase name must be in lowercase and contain only numbers, letters and hyphens"
                if len(val) == 0
                or not val.islower()
                or not val.replace("-", "").isalnum()
                else True
            ),
        ).ask()

        return kill_chain_phase
