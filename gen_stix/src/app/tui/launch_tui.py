"""This module is the entry point of the application in TUI mode."""

from textual.app import App
from gen_stix.src.app.tui.styles.my_app_css import MyAppCSS
from gen_stix.src.app.tui.screens.start_screen import StartScreen
from gen_stix.src.app.tui.screens.home_screen import HomeScreen


class LaunchTUI(App):

    CSS = MyAppCSS
    ENABLE_COMMAND_PALETTE = False

    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        ("tab", "focus_next", "Focus Next"),
        ("shift+tab", "focus_previous", "Focus Previous"),
    ]

    def __init__(self, projects_path: str):
        self.projects_path = projects_path
        self.session = None
        super().__init__()

    def on_mount(self):
        if self.session is None:
            start_screen = StartScreen(self.projects_path)
            self.push_screen(start_screen)
        else:
            home_screen = HomeScreen()
            self.push_screen(home_screen)

    def pop_screen(self):
        super().pop_screen()
        self.on_mount()

    def kill_session(self) -> None:
        self.projects_path = None
        self.pop_screen()
