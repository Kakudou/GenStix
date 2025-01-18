""" This module is the entry point for the command line interface. """

from gen_stix.src.app.cli import view as v


class OrderedGroup(v.click.Group):
    def __init__(self, name=None, commands=None, **attrs):
        super(OrderedGroup, self).__init__(name, commands, **attrs)
        self.commands = commands or v.collections.OrderedDict()

    def list_commands(self, ctx):
        return self.commands


class LaunchCLI:
    CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

    @v.click.group(
        help=f"CLI tool for generating and bundling STIX 2.1 objects., version {v.VERSION}",
        cls=OrderedGroup,
        context_settings=CONTEXT_SETTINGS,
    )
    def start():
        pass

    @start.command()
    def ______________________usage______________________():
        pass

    @start.command(short_help="Quick and simple usage of the tool.")
    def usage():
        v.click.echo(
            """
        You can use this tool following forms providing the informations if you want to be a little guided.
        Firstly, you need to create a project, it's gonna define where the STIX 2.1 objects will be stored.
           This allow you to create different projects for different purposes.
        Then when accessing a project, you will have the possibility to create, read, update and delete STIX 2.1 objects.

        But, if you want to use the tool without being guided, you can provide the informations directly in the command line.
        That's gonna be faster and more efficient, but you can only provide the required informations.
        You will need to update the object through the form if you want to add more informations.

        The option "-d" or "--projects-path" is optional, if not provided it will create the project in the path define in .config.yml file.

        Example to create a project:
            > GenStix create-project -p ProjectTest -d /home/GenStix/Workspace
        This will create a project named ProjectTest in the directory /home/GenStix/Workspace

        To create a STIX 2.1 object, let's say a KillChainPhase for example:
            > GenStix create-kill-chain-phase -p ProjectTest --kill-chain-name "kill-chain-name" --phase-name "phase-name"

        Another example to create a more complexe object, like the SDO AttackPattern:
            > GenStix create-attack-pattern -p ProjectTest

        You can do that for any commands, just provide the informations needed in the command line.
        You can access a command help by adding --help at the end of the command, to see the informations needed.
            > GenStix create-attack-pattern --help
        """
        )

    @start.command()
    def ______________________Projects______________________():
        pass

    @start.command(short_help="Create a Project to store STIX 2.1 objects.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project.",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="(Optional) The dir of the project.",
    )
    def create_project(project_name, projects_path):
        """Create a new project who will hold all the STIX 2.1 objects in a contextually relevant way."""
        v.click.echo(
            "let's create a new project to store our STIX 2.1 objects."
        )
        v.CreateProject.show(project_name, projects_path)

    @start.command(short_help="Access a Project.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project.",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="(Optional) The dir of the project.",
    )
    def access_project(project_name, projects_path):
        """Access a project"""
        v.click.echo(
            "Let's access that project and see the STIX 2.1 objects inside."
        )

        v.ReadProject.show(project_name, projects_path)

    @start.command(short_help="Delete a Project.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="The dir of the yaml files",
    )
    def delete_project(project_name, projects_path):
        """Delete a project"""
        v.click.echo("Let's delete a project")
        v.DeleteProject.show(project_name, projects_path)

    @start.command()
    def ______________________CDTs______________________():
        pass

    @start.command()
    def ______________________KillChainPhase______________________():
        pass

    @start.command(short_help="Create a Kill Chain Phase.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project.",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="(Optional) The dir of the project.",
    )
    @v.click.option(
        "--kill-chain-name",
        "kill_chain_name",
        help="(Required) The name of the kill chain.",
    )
    @v.click.option(
        "--phase-name",
        "phase_name",
        help="(Required) The name of the phase.",
    )
    def create_kill_chain_phase(
        project_name, projects_path, kill_chain_name, phase_name
    ):
        """Create a new Kill Chain Phase."""
        v.click.echo("Creating a new Kill Chain Phase.")
        v.CreateKillChainPhase.show(
            project_name, projects_path, kill_chain_name, phase_name
        )

    @start.command(short_help="Access a Kill Chain Phase.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project.",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="(Optional) The dir of the project.",
    )
    @v.click.option(
        "--kill-chain-name",
        "kill_chain_name",
        help="(Required) The name of the kill chain.",
    )
    @v.click.option(
        "--phase-name",
        "phase_name",
        help="(Required) The name of the phase.",
    )
    def access_kill_chain_phase(
        project_name, projects_path, kill_chain_name, phase_name
    ):
        """Access a Kill Chain Phase."""
        v.click.echo("Accessing a Kill Chain Phase.")
        v.ReadKillChainPhase.show(
            project_name, projects_path, kill_chain_name, phase_name
        )

    @start.command(short_help="Delete a Kill Chain Phase.")
    @v.click.option(
        "-p",
        "--project",
        "project_name",
        help="The name of the targeted project.",
    )
    @v.click.option(
        "-d",
        "--projects-path",
        "projects_path",
        help="(Optional) The dir of the project.",
    )
    @v.click.option(
        "--kill-chain-name",
        "kill_chain_name",
        help="(Required) The name of the kill chain.",
    )
    @v.click.option(
        "--phase-name",
        "phase_name",
        help="(Required) The name of the phase.",
    )
    def delete_kill_chain_phase(
        project_name, projects_path, kill_chain_name, phase_name
    ):
        """Delete a Kill Chain Phase."""
        v.click.echo("Deleting a Kill Chain Phase.")
        v.DeleteKillChainPhase.show(
            project_name, projects_path, kill_chain_name, phase_name
        )
