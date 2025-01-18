from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static, Button
from textual.containers import Grid
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from textual._node_list import DuplicateIds
from os import makedirs
from textual.screen import ModalScreen


class CreateProjectWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.create_project_form()
        self.error = None

    def compose(self) -> ComposeResult:
        """Compose the widget layout."""
        yield Label("Create a new project")
        yield self.project_name_field

    def on_mount(self):
        """Focus on the project name field when the widget is mounted."""
        self.project_name_field.focus()

    def create_project_form(self):
        """Create and initialize the project name input field."""
        self.project_name_field = CustomInputField(
            title="Project name",
            placeholder="Enter the project name",
            title_align="left",
        )

    async def submit_execute(self):
        """Handle the submission process."""
        validation_error = await self.validate_project_name()
        if validation_error is None:
            await self.create_project(
                project_name=self.project_name_field.content,
                project_path=self.app.session.get("projects_path", ""),
            )

    async def validate_project_name(self):
        """Validate the project name."""
        if self.project_name_field.content == "":
            await self._load_error(
                "Project name cannot be empty.", self.project_name_field
            )
            return False
        return None  # No error, project name is valid

    async def on_key(self, event):
        """Handle key events (e.g., 'enter' key to submit)."""
        if event.key == "enter":
            await self.submit_execute()

    async def create_project(self, project_name: str, project_path: str):
        """Create the project directory and update the navigation."""
        try:
            project_dir = f"{project_path}/{project_name}"
            makedirs(project_dir)

            with open(f"{project_path}/.projects", "a") as f:
                f.write(f"{project_name}\n")

            self.app.session["project_name"] = project_name
            self.app.screen.reload_navigation_tree()

            self.app.push_screen(
                ValidationModal(
                    f"Project `{project_name}` created at `{project_path}`.",
                    project_path,
                )
            )

        except OSError:
            self.app.push_screen(
                ValidationModal(
                    f"Project `{project_name}` already exists at `{project_path}`.",
                    project_path,
                )
            )

        finally:
            self.app.action_focus_previous()

    async def _load_error(self, error_message: str, before_widget: Widget):
        """Load and display an error message before the given widget."""
        await self.remove_error_widget()  # Ensure no previous error widget exists
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
