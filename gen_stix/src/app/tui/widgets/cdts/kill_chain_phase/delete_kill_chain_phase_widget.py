from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField

from gen_stix.src.app.adapter.cdts.kill_chain_phase.delete_kill_chain_phase.delete_kill_chain_phase_adapter import (
    DeleteKillChainPhaseAdapter,
)
from gen_stix.src.app.adapter.cdts.kill_chain_phase.list_kill_chain_phase.list_kill_chain_phase_adapter import (
    ListKillChainPhaseAdapter,
)

from gen_stix.src import STORAGE_ENGINE


class DeleteKillChainPhaseWidget(Widget):
    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.error = None
        self.target = target
        if self.target.label.plain == "Kill Chain Phase":
            self.delete_all_kill_chain_phase_form()
        else:
            self.delete_kill_chain_phase_form()

    def compose(self) -> ComposeResult:
        yield Label("Delete a kill chain phase")
        if self.target.label.plain == "Kill Chain Phase":
            yield self.all_deletion_validation
        else:
            yield self.kill_chain_name_field
            yield self.phase_name_field

    def on_mount(self):
        if self.target.label.plain == "Kill Chain Phase":
            self.all_deletion_validation.focus()
        else:
            self.kill_chain_name_field.focus()

    def delete_kill_chain_phase_form(self):
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

    def delete_all_kill_chain_phase_form(self):
        """Create and initialize input fields for the form."""
        self.all_deletion_validation = CustomInputField(
            title="Are you sure you want to delete all kill chain phases? (yes/no)",
            placeholder="Enter 'yes' to confirm",
            title_align="left",
            auto_focus=False,
        )

    async def submit_execute(self):
        """Validate inputs and execute the deletion of the kill chain phase."""
        if self.target.label.plain == "Kill Chain Phase":
            if self.all_deletion_validation.content == "yes":
                for kill_chain in (
                    ListKillChainPhaseAdapter()
                    .execute({}, STORAGE_ENGINE)
                    .all_kill_chain_phases
                ):
                    kill_chain_name, phase_name = kill_chain.split(" - ")
                    await self.delete_kill_chain_phase(
                        kill_chain_name=kill_chain_name,
                        phase_name=phase_name,
                    )
        else:
            error = await self.validate_kill_chain_phase()
            if error is None:
                await self.delete_kill_chain_phase(
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

        target_kill_chain_name = self.target.label.plain.split(" - ")[0]
        if self.kill_chain_name_field.content != target_kill_chain_name:
            await self._load_error(
                "Kill chain name does not match the current kill chain",
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

        target_phase_name = self.target.label.plain.split(" - ")[1]
        if self.phase_name_field.content != target_phase_name:
            await self._load_error(
                "Phase name does not match the current phase",
                self.phase_name_field,
                "phase_name_error",
            )
            return False

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter":
            await self.submit_execute()
            if self.target.label.plain == "Kill Chain Phase":
                if not self.all_deletion_validation.has_focus:
                    self.app.action_focus_next()
            else:
                if not self.phase_name_field.has_focus:
                    self.app.action_focus_next()

    async def delete_kill_chain_phase(self, kill_chain_name, phase_name):
        """Delete the kill chain phase."""
        inputs = {
            "kill_chain_name": kill_chain_name,
            "phase_name": phase_name,
        }
        adapter = DeleteKillChainPhaseAdapter().execute(inputs, STORAGE_ENGINE)

        if adapter.error is not None:
            await self._load_error(
                adapter.error, self.kill_chain_name_field, "error"
            )
        else:
            await self.app.screen.action_clear_stat()
            self.app.screen._load_data_for_stix("Kill Chain Phase")
            self.app.screen.navigation_tree.find_child("Kill Chain Phase")

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
