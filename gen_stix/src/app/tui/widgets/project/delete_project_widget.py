from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static, Button
from textual.containers import Grid
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from textual._node_list import DuplicateIds
from textual.screen import ModalScreen
from shutil import rmtree


class DeleteProjectWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.target = target
        self.error = None
        self.create_delete_project_form()

    def compose(self) -> ComposeResult:
        """Compose the widget layout."""
        yield Label("To delete a project, enter the project name")
        yield self.project_name_field

    def on_mount(self):
        """Focus on the project name field when the widget is mounted."""
        self.project_name_field.focus()

    def create_delete_project_form(self):
        """Create and initialize the project name input field."""
        self.project_name_field = CustomInputField(
            title="Project name",
            placeholder="Enter the project name to be deleted",
            title_align="left",
        )

    async def submit_execute(self):
        """Handle the submission process."""
        validation_error = await self.validate_project_name()
        if validation_error is None:
            await self.delete_project(
                project_name=self.project_name_field.content,
                project_path=self.app.session.get("projects_path", ""),
            )

    async def validate_project_name(self):
        """Validate the project name."""
        if not self.project_name_field.content:
            await self._load_error(
                "Project name cannot be empty.", self.project_name_field
            )
            return False
        elif self.project_name_field.content != self.target:
            await self._load_error(
                "Project name does not match the current project.",
                self.project_name_field,
            )
            return False
        return None

    async def on_key(self, event):
        """Handle key events (e.g., 'enter' key to submit)."""
        if event.key == "enter":
            await self.submit_execute()

    async def delete_project(self, project_name: str, project_path: str):
        """Delete the project and update the navigation."""
        try:
            print(f"Deleting project {project_name} at {project_path}")
            project_dir = f"{project_path}/{project_name}"

            rmtree(project_dir, ignore_errors=True)

            self._remove_project_from_file(project_name, project_path)

            self.app.session["project_name"] = project_name
            self.app.screen.reload_navigation_tree()

            self.app.push_screen(
                ValidationModal(
                    f"Project `{project_name}` deleted from `{project_path}`.",
                    project_path,
                )
            )

        except Exception as e:
            print(f"Error deleting project: {e}")
            self.app.push_screen(
                ValidationModal(
                    f"Failed to delete project `{project_name}` at `{project_path}`.",
                    project_path,
                )
            )
        finally:
            self.app.action_focus_previous()

    def _remove_project_from_file(self, project_name: str, project_path: str):
        """Remove the project name from the .projects file."""
        with open(f"{project_path}/.projects", "r") as f:
            lines = f.readlines()

        with open(f"{project_path}/.projects", "w") as f:
            for line in lines:
                if line.strip("\n") != project_name:
                    f.write(line)

    async def _load_error(self, error_message: str, before_widget: Widget):
        """Load and display an error message before the given widget."""
        await self.remove_error_widget()
        self.mount(
            Static(error_message, id="error", classes="error"),
            before=before_widget,
        )

    async def remove_error_widget(self):
        """Remove any existing error widget."""
        try:
            await self.get_widget_by_id("error").remove()
        except (DuplicateIds, NoMatches):
            pass


class ValidationModal(ModalScreen):

    def __init__(self, message: str, path: str):
        super().__init__()
        self.message = message
        self.path = path

    def compose(self):
        """Compose the modal screen layout."""
        yield Grid(
            Label(self.message, id="ValidationModal"),
            Button.success("Return", id="return", classes="center-button"),
            id="Modal",
        )

    async def on_key(self, event):
        """Handle key events in the modal screen."""
        if event.key == "enter":
            self.app.pop_screen()
            await self.app.action_simulate_key("enter")
