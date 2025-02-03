from json import dumps as json_dumps
from textual.widget import Widget
from textual.css.query import NoMatches
from textual.widgets import Markdown
from textual.app import ComposeResult
from textual.widgets import Label, Static
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField

from gen_stix.src.app.adapter.cdts.external_reference.read_external_reference.read_external_reference_adapter import (
    ReadExternalReferenceAdapter,
)

from gen_stix.src import STORAGE_ENGINE


class ReadExternalReferenceWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.target = target
        if self.target.label.plain == "External Reference":
            self.app.screen.navigation_tree.current_node.expand()
            self.ask_for_external_reference()
        else:
            self.app.screen.navigation_tree.focus_child(
                self.app.screen.navigation_tree.current_node.label.plain
            )
            self.read_external_reference(
                source_name=self.target.label.plain.split(" - ")[0],
                external_id=self.target.label.plain.split(" - ")[1],
            )

    def compose(self) -> ComposeResult:
        yield Label("Read a External Reference")
        yield self.source_name_field
        yield self.external_id_field
        if self.target.label.plain != "External Reference":
            yield self.json_field

    def on_mount(self):
        self.source_name_field.focus()

    def ask_for_external_reference(self):
        """Create and initialize input fields for the form."""

        self.source_name_field = CustomInputField(
            title="Source name",
            placeholder="Enter the source name",
            title_align="left",
            auto_focus=False,
        )
        self.external_id_field = CustomInputField(
            title="External id",
            placeholder="Enter the external id",
            title_align="left",
            auto_focus=False,
        )

    async def submit_execute(self):
        """Validate inputs and execute the read of the kill chain phase."""
        if self.target.label.plain == "External Reference":
            error = await self.validate_external_reference()
            if error is None:
                inputs = {
                    "source_name": self.source_name_field.content,
                    "external_id": self.external_id_field.content,
                }
                contract = ReadExternalReferenceAdapter().execute(
                    inputs, STORAGE_ENGINE
                )
                if contract.error is not None:
                    await self._load_error(
                        contract.error,
                        self.source_name_field,
                        "source_name_error",
                    )
                else:
                    self.read_external_reference(
                        source_name=contract.source_name,
                        external_id=contract.external_id,
                    )
                    self.app.screen.navigation_tree.find_child(
                        f"{contract.source_name} - {contract.external_id}"
                    )
                    new_target = self.app.screen.navigation_tree.current_node
                    await self.app.screen.action_clear_stat()
                    self.app.screen.navigation_tree.focus_child(
                        new_target.label.plain
                    )
                    self.app.simulate_key("r")

    async def validate_external_reference(self):
        """Validate the kill chain and external ids."""
        # Remove previous error widgets
        await self.remove_errors()

        if self.source_name_field.content == "":
            await self._load_error(
                "Source name cannot be empty",
                self.source_name_field,
                "source_name_error",
            )
            return False

        if self.external_id_field.content == "":
            await self._load_error(
                "External id cannot be empty",
                self.external_id_field,
                "external_id_error",
            )
            return False

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter":
            await self.submit_execute()
            if not self.external_id_field.has_focus:
                self.app.action_focus_next()

    def read_external_reference(self, source_name, external_id):
        """Create and initialize input fields for the form."""

        inputs = {
            "source_name": source_name,
            "external_id": external_id,
        }
        stix_representation = None

        contract = ReadExternalReferenceAdapter().execute(
            inputs, STORAGE_ENGINE
        )

        if contract.error is not None:
            return

        source_name = contract.source_name
        external_id = contract.external_id
        stix_representation = contract.stix_representation

        self.source_name_field = CustomInputField(
            title="Source name",
            title_align="left",
            auto_focus=False,
            content=source_name,
            disabled=True,
        )
        self.external_id_field = CustomInputField(
            title="External id",
            title_align="left",
            auto_focus=False,
            content=external_id,
            disabled=True,
        )
        self.json_field = Markdown(
            markdown=f"```json\n{json_dumps(stix_representation, indent=2)}\n```",
        )

    async def remove_errors(self):
        """Remove error widgets from the form."""
        for error_id in [
            "source_name_error",
            "external_id_error",
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
