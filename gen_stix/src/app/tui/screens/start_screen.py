"""This module will handle the start screen of the application, where the user will be able to select the projects workpspace."""

from os import makedirs, path
from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static, Collapsible, Label

from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from gen_stix.src.app.repository.infile.infile_persist import InFilePersist


class StartScreen(Screen):
    """This class will handle the start screen of the application, where the user will be able to select the projects workpspace."""

    def __init__(self, projects_path: str | None):
        """Constructor of the class."""
        super().__init__()
        self.app.title = "GenSTIX TUI - Start Screen"
        self.init_form(projects_path)
        self.error = None

    def init_form(self, projects_path: str):
        """Method to initialize the form."""
        self.header = Header(show_clock=True)

        self.projects_path_field = CustomInputField(
            "Projects Path", projects_path, placeholder="Projects path"
        )
        self.submit_button = Button("Submit", variant="primary", id="submit")
        self.footer = Footer()

    def on_mount(self):
        """Method to be executed when the screen is mounted."""
        self.projects_path_field.focus()
        if self.app.session is not None:
            self.submit_execute()
        if self.error is not None:
            self.mount(
                Static(self.error, id="error", classes="error"),
                before=self.projects_path_field,
            )
            self.error = None

    def compose(self) -> ComposeResult:
        """Method to compose the screen."""
        yield self.header
        with Collapsible(
            collapsed=False,
            title="The Projects Path is the path where all the projects will be saved",
        ):
            yield Label("If it doesn't exist, it will be created")
        yield self.projects_path_field
        yield self.submit_button
        yield self.footer

    def submit_execute(self):
        if self.projects_path_field.content != "":
            inputs = {
                "projects_path": self.projects_path_field.content,
            }

            if not path.isdir(inputs["projects_path"]):
                self.error = f"The projects path {inputs['projects_path']} does not exist."
                self.app.session = inputs
                self.app.push_screen(
                    YesNoModalScreen(
                        "The projects path does not exist. Do you want to create it?",
                        inputs["projects_path"],
                    )
                )

            if self.error is None:
                self.app.session = inputs
                ifr = InFilePersist()
                ifr.save_path = inputs["projects_path"]
            else:
                self.error = "Error for accessing the projects path."
        else:
            self.error = "Please provide the projects path."

        if self.error is None:
            self.app.pop_screen()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "submit":
            self.submit_execute()


class YesNoModalScreen(ModalScreen):

    def __init__(self, message: str, path: str):
        super().__init__()
        self.message = message
        self.path = path

    def compose(self):
        yield Grid(
            Label(self.message, id="YesNoQuestion"),
            Button.success("Yes", id="yes"),
            Button.error("No", id="no"),
            id="Modal",
        )

    def on_key(self, event):
        if event.key == "left":
            self.focus_previous()
        elif event.key == "right":
            self.focus_next()
        elif event.key == "enter":
            self.on_button_pressed(Button.Pressed(self.focused))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            makedirs(f"{self.path}", exist_ok=True)
            self.app.pop_screen()
        elif event.button.id == "no":
            self.app.session = None
            self.app.pop_screen()
            self.app.screen.error = f"The projects path {self.path} does not exist, and it was not created."
