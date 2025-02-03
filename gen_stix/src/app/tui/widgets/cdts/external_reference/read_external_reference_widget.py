from rich.text import Text
from textual.containers import Container
from json import dumps as json_dumps
from textual.widget import Widget
from textual.css.query import NoMatches
from textual.widgets import Markdown
from textual.app import ComposeResult
from textual.widgets import Label, Static, Input
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from gen_stix.src.app.tui.widgets._autocomplete import (
    AutoComplete,
    Dropdown,
    DropdownItem,
)

from gen_stix.src.app.adapter.cdts.external_reference.read_external_reference.read_external_reference_adapter import (
    ReadExternalReferenceAdapter,
)

from gen_stix.src import STORAGE_ENGINE
from gen_stix.src.gen_stix.entity.enums.external_reference_capec import (
    ExternalReferenceCapec,
)


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

    def get_capec_items(self, input_state):
        items = []

        for member in ExternalReferenceCapec:
            id_value = member.value
            name_value = member.name  # This calls the custom name property
            items.append(DropdownItem(name_value, Text(str(id_value))))

        matches = [
            c
            for c in items
            if input_state.value.lower() in c.main.plain.lower()
        ]
        ordered = sorted(
            matches,
            key=lambda v: v.main.plain.startswith(input_state.value.lower()),
        )

        return ordered

    def compose(self) -> ComposeResult:
        yield Label("Read a External Reference")
        yield self.source_name_field
        if (
            self.source_name_field.content.lower() == "capec"
            and self.target.label.plain == "External Reference"
        ):
            self.external_id_field_autocomplete = AutoComplete(
                Input(placeholder="Enter the external id", id="select"),
                Dropdown(items=self.get_capec_items),
                title="External ID",
                tab_moves_focus=True,
                tooltip_text="""If the source name is CAPEC, the external id must be a CAPEC.""",
            )
            self.external_id_field = self.external_id_field_autocomplete
        else:
            self.external_id_field = self.external_id_field_custom

        yield self.external_id_field
        if self.target.label.plain != "External Reference":
            yield self.description_field
            yield self.url_field
            yield Container(
                self.hashes_algo_field,
                self.hashes_value_field,
                id="horizontal-layout",
            )
            yield self.json_field

    def on_mount(self):
        self.source_name_field.focus()

    def ask_for_external_reference(self):
        """Create and initialize input fields for the form."""

        self.source_name_field = CustomInputField(
            title="Source name",
            placeholder="Enter the source name",
            title_align="left",
            auto_focus=True,
            required=True,
            tooltip_text="""The name of the source of the external reference.""",
        )
        self.external_id_field_custom = CustomInputField(
            title="External id",
            placeholder="Enter the external id",
            title_align="left",
            auto_focus=True,
            required=True,
            tooltip_text="""An identifier for the external reference content.""",
        )

    async def submit_execute(self):
        """Validate inputs and execute the read of the kill chain phase."""
        if self.target.label.plain == "External Reference":
            error = await self.validate_external_reference()
            if error is None:
                if isinstance(self.external_id_field, CustomInputField):
                    external_id_content = self.external_id_field.content
                else:
                    external_id_content = self.external_id_field.input.value

                inputs = {
                    "source_name": self.source_name_field.content,
                    "external_id": external_id_content,
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
                    if contract.source_name.lower() == "capec":
                        if contract.external_id.lower().startswith("capec-"):
                            external_id = ExternalReferenceCapec.from_id(
                                contract.external_id.split("CAPEC-")[1]
                            ).name

                    self.read_external_reference(
                        source_name=contract.source_name,
                        external_id=external_id,
                    )
                    self.app.screen.navigation_tree.find_child(
                        f"{contract.source_name} - {external_id}"
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
        elif self.source_name_field.content.lower() == "capec" and isinstance(
            self.external_id_field, CustomInputField
        ):
            await self._load_error(
                "External id must be a CAPEC id",
                self.source_name_field,
                "source_name_error",
            )
            await self.recompose()
            return False
        elif self.source_name_field.content.lower() != "capec" and isinstance(
            self.external_id_field, AutoComplete
        ):
            await self.recompose()
            await self.app.action_simulate_key("tab")
            return False

        external_id_content = ""
        if isinstance(self.external_id_field, CustomInputField):
            external_id_content = self.external_id_field.content
        else:
            external_id_content = self.external_id_field.input.value
        if external_id_content == "":
            await self._load_error(
                "External id cannot be empty",
                self.external_id_field,
                "external_id_error",
            )
            return False
        else:
            if isinstance(self.external_id_field, AutoComplete):
                if not ExternalReferenceCapec.from_name(
                    self.external_id_field.input.value
                ):
                    await self._load_error(
                        "External id must be a known CAPEC id",
                        self.external_id_field,
                        "external_id_error",
                    )
                    return False

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter" or event.key == "tab":
            await self.submit_execute()

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
        description = contract.description
        url = contract.url
        hashes = contract.hashes
        stix_representation = contract.stix_representation

        if source_name.lower() == "capec":
            external_id = ExternalReferenceCapec.from_id(
                external_id.split("CAPEC-")[1]
            ).name

        self.source_name_field = CustomInputField(
            title="Source name",
            title_align="left",
            auto_focus=False,
            content=source_name,
            disabled=True,
        )
        self.external_id_field_custom = CustomInputField(
            title="External id",
            title_align="left",
            auto_focus=False,
            content=external_id,
            disabled=True,
        )
        self.description_field = CustomInputField(
            title="Description",
            title_align="left",
            auto_focus=False,
            content=description,
            disabled=True,
        )

        self.url_field = CustomInputField(
            title="URL",
            title_align="left",
            auto_focus=False,
            content=url,
            disabled=True,
        )

        self.hashes_algo_field = CustomInputField(
            title="Hash Algorithm",
            title_align="left",
            auto_focus=False,
            id="hashes_algo_field",
            classes="hashes_fields",
            content=hashes[0]["algorithm"] if hashes else "",
            disabled=True,
        )

        self.hashes_value_field = CustomInputField(
            title="Hash",
            title_align="left",
            auto_focus=False,
            id="hashes_value_field",
            classes="hashes_fields",
            content=hashes[0]["value"] if hashes else "",
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
