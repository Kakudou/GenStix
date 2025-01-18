"""This module handle the form to select a project and set the path to save it"""

from sys import exit

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

from gen_stix.src.app.cli.view.main_menu import MainMenu
from gen_stix.src.app.cli.view.factory import Factory

import questionary


class ReadProject:

    @staticmethod
    def show(wanted_project=None, project_dir=None, referer=None):
        ifr = InFilePersist()

        if project_dir is None:
            project_dir = questionary.path(
                "Enter the path to the directory where the projects are saved:",
                default=f"{ifr.save_path}",
            ).ask()

        project_name = ReadProject.select_project(wanted_project, project_dir)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {project_dir}.")
            exit(1)
        else:
            print(f"The project selected is: {project_name}")
            print(
                f"The project will be saved in: {project_dir}/{project_name}"
            )

        if project_dir is not None:
            ifr.save_path = f"{project_dir}/{project_name}"

        MainMenu.show(
            referer=referer,
            project_name=project_name,
            projects_path=project_dir,
        )

    @staticmethod
    def select_project(wanted_project=None, project_dir=None):

        try:
            with open(f"{project_dir}/.projects", "r") as f:
                all_projects = f.read().splitlines()
        except FileNotFoundError:
            print(f"\r\nI can't find any project in: {project_dir}")
            exit(1)

        if wanted_project is None or wanted_project not in all_projects:
            project_name = Factory.paginated_list_factory(
                all_projects, "The Projects"
            )
        elif wanted_project in all_projects:
            project_name = wanted_project
        else:
            project_name = None

        return project_name
