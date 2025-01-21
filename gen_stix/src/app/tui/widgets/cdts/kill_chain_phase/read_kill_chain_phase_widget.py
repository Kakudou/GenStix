from json import dumps as json_dumps
from textual.widget import Widget
from textual.css.query import NoMatches
from textual.widgets import Markdown
from textual.app import ComposeResult
from textual.widgets import Label, Static
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField

from gen_stix.src.app.adapter.cdts.kill_chain_phase.read_kill_chain_phase.read_kill_chain_phase_adapter import (
    ReadKillChainPhaseAdapter,
)

from gen_stix.src import STORAGE_ENGINE


class ReadKillChainPhaseWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.target = target
        from gen_stix.src.utils.debug import Debug

        print(f"Debug: {Debug.dump(self.app.screen.navigation_tree)}")
        if self.target.label.plain == "Kill Chain Phase":
            self.app.screen.navigation_tree.current_node.expand()
            self.ask_for_kill_chain_phase()
        else:
            self.app.screen.navigation_tree.focus_child(
                self.app.screen.navigation_tree.current_node.label.plain
            )
            self.read_kill_chain_phase(
                kill_chain_name=self.target.label.plain.split(" - ")[0],
                phase_name=self.target.label.plain.split(" - ")[1],
            )

    def compose(self) -> ComposeResult:
        yield Label("Read a Kill Chain Phase")
        yield self.kill_chain_name_field
        yield self.phase_name_field
        if self.target.label.plain != "Kill Chain Phase":
            yield self.json_field

    def on_mount(self):
        self.kill_chain_name_field.focus()

    def ask_for_kill_chain_phase(self):
        """Create and initialize input fields for the form."""

        self.kill_chain_name_field = CustomInputField(
            title="Kill chain name",
            placeholder="Enter the kill chain name",
            title_align="left",
            auto_focus=False,
        )
        self.phase_name_field = CustomInputField(
            title="Phase name",
            placeholder="Enter the phase name",
            title_align="left",
            auto_focus=False,
        )

    async def submit_execute(self):
        """Validate inputs and execute the read of the kill chain phase."""
        if self.target.label.plain == "Kill Chain Phase":
            error = await self.validate_kill_chain_phase()
            if error is None:
                inputs = {
                    "kill_chain_name": self.kill_chain_name_field.content,
                    "phase_name": self.phase_name_field.content,
                }
                contract = ReadKillChainPhaseAdapter().execute(
                    inputs, STORAGE_ENGINE
                )
                if contract.error is not None:
                    await self._load_error(
                        contract.error,
                        self.kill_chain_name_field,
                        "kill_chain_name_error",
                    )
                else:
                    self.read_kill_chain_phase(
                        kill_chain_name=contract.kill_chain_name,
                        phase_name=contract.phase_name,
                    )
                    self.app.screen.navigation_tree.find_child(
                        f"{contract.kill_chain_name} - {contract.phase_name}"
                    )
                    new_target = self.app.screen.navigation_tree.current_node
                    await self.app.screen.action_clear_stat()
                    self.app.screen.navigation_tree.focus_child(
                        new_target.label.plain
                    )
                    self.app.simulate_key("r")

    async def validate_kill_chain_phase(self):
        """Validate the kill chain and phase names."""
        # Remove previous error widgets
        await self.remove_errors()

        if self.kill_chain_name_field.content == "":
            await self._load_error(
                "Kill chain name cannot be empty",
                self.kill_chain_name_field,
                "kill_chain_name_error",
            )
            return False

        if self.phase_name_field.content == "":
            await self._load_error(
                "Phase name cannot be empty",
                self.phase_name_field,
                "phase_name_error",
            )
            return False

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter":
            await self.submit_execute()
            if not self.phase_name_field.has_focus:
                self.app.action_focus_next()

    def read_kill_chain_phase(self, kill_chain_name, phase_name):
        """Create and initialize input fields for the form."""

        inputs = {
            "kill_chain_name": kill_chain_name,
            "phase_name": phase_name,
        }
        stix_representation = None

        contract = ReadKillChainPhaseAdapter().execute(inputs, STORAGE_ENGINE)

        if contract.error is not None:
            return

        kill_chain_name = contract.kill_chain_name
        phase_name = contract.phase_name
        stix_representation = contract.stix_representation

        self.kill_chain_name_field = CustomInputField(
            title="Kill chain name",
            title_align="left",
            auto_focus=False,
            content=kill_chain_name,
            disabled=True,
        )
        self.phase_name_field = CustomInputField(
            title="Phase name",
            title_align="left",
            auto_focus=False,
            content=phase_name,
            disabled=True,
        )
        self.json_field = Markdown(
            markdown=f"```json\n{json_dumps(stix_representation, indent=2)}\n```",
        )

    async def remove_errors(self):
        """Remove error widgets from the form."""
        for error_id in [
            "kill_chain_name_error",
            "phase_name_error",
        ]:
            try:
                await self.get_widget_by_id(error_id).remove()
            except NoMatches:
                pass

    async def _load_error(self, error_message, before_widget, id):
        """Load an error message widget before the specified widget."""
        try:
            await self.get_widget_by_id(id).remove()
        except NoMatches:
            pass
        self.mount(
            Static(error_message, id=id, classes="error"), before=before_widget
        )
