from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from textual._node_list import DuplicateIds

from gen_stix.src.app.adapter.cdts.kill_chain_phase.create_kill_chain_phase.create_kill_chain_phase_adapter import (
    CreateKillChainPhaseAdapter,
)
from gen_stix.src.app.cli.entity_view.cdts.kill_chain_phase.kill_chain_phase_view import (
    KillChainPhaseView,
)

from gen_stix.src import STORAGE_ENGINE


class CreateKillChainPhaseWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.error = None
        self.create_kill_chain_phase_form()

    def compose(self) -> ComposeResult:
        yield Label("Create a new kill chain phase")
        yield self.kill_chain_name_field
        yield self.phase_name_field

    def on_mount(self):
        self.kill_chain_name_field.focus()

    def create_kill_chain_phase_form(self):
        """Create and initialize input fields for the form."""
        self.kill_chain_name_field = CustomInputField(
            title="Kill chain name",
            placeholder="Enter the kill chain name",
            title_align="left",
        )
        self.phase_name_field = CustomInputField(
            title="Phase name",
            placeholder="Enter the phase name",
            title_align="left",
        )

    async def submit_execute(self):
        """Validate inputs and execute the creation of the kill chain phase."""
        error = await self.validate_kill_chain_phase()
        if error is None:
            await self.create_kill_chain_phase(
                kill_chain_name=self.kill_chain_name_field.content,
                phase_name=self.phase_name_field.content,
            )

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

        if not self.kill_chain_name_field.content.replace("-", "").isalnum():
            await self._load_error(
                "Kill chain name must be in lowercase and contain only alphanumeric characters and hyphens",
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

        print(self.phase_name_field.content)
        print(self.phase_name_field.content.replace("-", ""))
        print(self.phase_name_field.content.replace("-", "").isalnum())
        if not self.phase_name_field.content.replace("-", "").isalnum():
            await self._load_error(
                "Phase name must be in lowercase and contain only alphanumeric characters and hyphens",
                self.phase_name_field,
                "phase_name_error",
            )
            return False

        return None

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter":
            await self.submit_execute()

    async def create_kill_chain_phase(
        self, kill_chain_name: str, phase_name: str
    ):
        """Create the kill chain phase and handle the result."""
        print(f"Kill chain name: {kill_chain_name}")
        print(f"Phase name: {phase_name}")

        inputs = {
            "kill_chain_name": kill_chain_name.lower(),
            "phase_name": phase_name.lower(),
        }
        await self.remove_errors()

        kill_chain = CreateKillChainPhaseAdapter.execute(
            inputs, STORAGE_ENGINE
        )

        if kill_chain.error:
            await self._load_error(
                kill_chain.error,
                self.kill_chain_name_field,
                id="error_duplicate",
            )
        else:
            self.app.screen.navigation_tree.add_leaf(
                "Kill Chain Phase",
                f"{kill_chain_name} - {phase_name}",
                f"{kill_chain_name} - {phase_name}",
            )
            print("Kill chain phase created successfully")
            kc_view = KillChainPhaseView.from_contract(kill_chain)
            print("The json representation of the kill chain phase is:")
            print(kc_view.stix_representation)

    async def remove_errors(self):
        """Remove error widgets from the form."""
        for error_id in [
            "kill_chain_name_error",
            "phase_name_error",
            "error_duplicate",
        ]:
            try:
                await self.get_widget_by_id(error_id).remove()
            except (DuplicateIds, NoMatches):
                pass

    async def _load_error(self, error_message, before_widget, id):
        """Load an error message widget before the specified widget."""
        try:
            await self.get_widget_by_id(id).remove()
        except (DuplicateIds, NoMatches):
            pass
        self.mount(
            Static(error_message, id=id, classes="error"), before=before_widget
        )
