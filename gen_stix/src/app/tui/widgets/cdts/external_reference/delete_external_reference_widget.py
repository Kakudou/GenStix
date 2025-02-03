from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField

from gen_stix.src.app.adapter.cdts.external_reference.delete_external_reference.delete_external_reference_adapter import (
    DeleteExternalReferenceAdapter,
)
from gen_stix.src.app.adapter.cdts.external_reference.list_external_reference.list_external_reference_adapter import (
    ListExternalReferenceAdapter,
)

from gen_stix.src import STORAGE_ENGINE


class DeleteExternalReferenceWidget(Widget):
    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.error = None
        self.target = target
        if self.target.label.plain == "External Reference":
            self.delete_all_external_reference_form()
        else:
            self.delete_external_reference_form()

    def compose(self) -> ComposeResult:
        yield Label("Delete a kill chain phase")
        if self.target.label.plain == "External Reference":
            yield self.all_deletion_validation
        else:
            yield self.source_name_field
            yield self.external_id_field

    def on_mount(self):
        if self.target.label.plain == "External Reference":
            self.all_deletion_validation.focus()
        else:
            self.source_name_field.focus()

    def delete_external_reference_form(self):
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

    def delete_all_external_reference_form(self):
        """Create and initialize input fields for the form."""
        self.all_deletion_validation = CustomInputField(
            title="Are you sure you want to delete all kill chain phases? (yes/no)",
            placeholder="Enter 'yes' to confirm",
            title_align="left",
            auto_focus=False,
        )

    async def submit_execute(self):
        """Validate inputs and execute the deletion of the kill chain phase."""
        if self.target.label.plain == "External Reference":
            if self.all_deletion_validation.content == "yes":
                for kill_chain in (
                    ListExternalReferenceAdapter()
                    .execute({}, STORAGE_ENGINE)
                    .all_external_references
                ):
                    source_name, external_id = kill_chain.split(" - ")
                    await self.delete_external_reference(
                        source_name=source_name,
                        external_id=external_id,
                    )
        else:
            error = await self.validate_external_reference()
            if error is None:
                await self.delete_external_reference(
                    source_name=self.source_name_field.content,
                    external_id=self.external_id_field.content,
                )

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

        target_source_name = self.target.label.plain.split(" - ")[0]
        if self.source_name_field.content != target_source_name:
            await self._load_error(
                "Source name does not match the current kill chain",
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

        target_external_id = self.target.label.plain.split(" - ")[1]
        if self.external_id_field.content != target_external_id:
            await self._load_error(
                "External id does not match the current phase",
                self.external_id_field,
                "external_id_error",
            )
            return False

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter":
            await self.submit_execute()
            if self.target.label.plain == "External Reference":
                if not self.all_deletion_validation.has_focus:
                    self.app.action_focus_next()
            else:
                if not self.external_id_field.has_focus:
                    self.app.action_focus_next()

    async def delete_external_reference(self, source_name, external_id):
        """Delete the kill chain phase."""
        inputs = {
            "source_name": source_name,
            "external_id": external_id,
        }
        adapter = DeleteExternalReferenceAdapter().execute(
            inputs, STORAGE_ENGINE
        )

        if adapter.error is not None:
            await self._load_error(
                adapter.error, self.source_name_field, "error"
            )
        else:
            await self.app.screen.action_clear_stat()
            self.app.screen._load_data_for_stix("External Reference")
            self.app.screen.navigation_tree.find_child("External Reference")

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
