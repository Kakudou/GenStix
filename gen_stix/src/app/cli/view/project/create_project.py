"""This module handle the form and create a project from it"""

from os import makedirs
import questionary
from prompt_toolkit.shortcuts import CompleteStyle

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

from gen_stix.src.app.cli.view.main_menu import MainMenu


class CreateProject:

    @staticmethod
    def show(project_name=None, project_path=None):

        ifr = InFilePersist()
        if project_name is None:
            answers = CreateProject.create_project_form()

            print("")
            confirm = questionary.confirm(
                "Are you sure of the above inputs?", default=True
            ).ask()

            if not confirm:
                print("\r\n Ok, let's try again")
                CreateProject.show()

            path = answers["path"]
            name = answers["name"]
        else:
            if project_path is None:
                path = ifr.save_path
            else:
                path = project_path
            name = project_name

        print("Creating project...")
        print(f"The project will be created at {path}/{name}")

        try:
            makedirs(f"{path}/{name}")
            print(f"Project {name} created at {path}")
            print(
                f"a file name .projects was created at {path}, this file is used to store all the projects created"
            )
            with open(f"{path}/.projects", "a") as f:
                f.write(f"{name}\n")

            print("Project created successfully")
        except OSError:
            print(f"The project {name} already exists at {path}, using it.")

        if path is not None:
            ifr.save_path = f"{path}"

        MainMenu.show(projects_path=path, project_name=name)

    @staticmethod
    def create_project_form():

        project = {}

        project["name"] = questionary.text(
            "What's the project name?",
            validate=lambda val: (
                "That project need a name!" if len(val) == 0 else True
            ),
        ).ask()

        ifr = InFilePersist()

        project["path"] = questionary.path(
            "What's the path for this project?",
            complete_style=CompleteStyle.MULTI_COLUMN,
            validate=lambda val: (
                "That project need to be somewhere!" if len(val) == 0 else True
            ),
            only_directories=True,
            default=f"{ifr.save_path}",
        ).ask()

        return project
