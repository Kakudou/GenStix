"""This module handle the form to select a project and delete it"""

from sys import exit

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

import questionary
from shutil import rmtree
from gen_stix.src.app.cli.view.factory import Factory


class DeleteProject:

    @staticmethod
    def show(wanted_project=None, project_dir=None):

        if project_dir is None:
            ifr = InFilePersist()

            project_dir = questionary.path(
                "Enter the path to the directory where the projects are saved:",
                default=f"{ifr.save_path}",
            ).ask()

        project_name = DeleteProject.select_project(
            wanted_project, project_dir
        )

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {project_dir}.")
            exit(1)
        else:
            print(f"The project selected is: {project_name} at {project_dir}")
            print("The project will be deleted.")

            rmtree(f"{project_dir}/{project_name}", ignore_errors=True)
            with open(f"{project_dir}/.projects", "r") as f:
                lines = f.readlines()
            with open(f"{project_dir}/.projects", "w") as f:
                for line in lines:
                    if line.strip("\n") != project_name:
                        f.write(line)

            print(f"\r\nThe project {project_name} has been deleted.")
            exit(0)

    @staticmethod
    def select_project(wanted_project=None, project_dir=None):

        try:
            with open(f"{project_dir}/.projects", "r") as f:
                all_projects = f.readlines()
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
