from rich.text import Text
from textual.containers import Container
from textual.widget import Widget
from textual.css.query import NoMatches
from textual.app import ComposeResult
from textual.widgets import Label, Static, Input
from textual._node_list import DuplicateIds
from gen_stix.src.app.tui.widgets.custom_input_field import CustomInputField
from gen_stix.src.app.tui.widgets._autocomplete import (
    AutoComplete,
    Dropdown,
    DropdownItem,
)


from gen_stix.src.app.adapter.cdts.external_reference.create_external_reference.create_external_reference_adapter import (
    CreateExternalReferenceAdapter,
)

from gen_stix.src import STORAGE_ENGINE
from gen_stix.src.gen_stix.entity.enums.external_reference_capec import (
    ExternalReferenceCapec,
)
from gen_stix.src.gen_stix.entity.open_vocabulary.hashes_ov import HashesOV


class CreateExternalReferenceWidget(Widget):

    def __init__(self, id: str, classes: str = "", target=None):
        super().__init__(id=id, classes=classes)
        self.error = None
        self.create_external_reference_form()
        self.target = target

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

    def get_hashes_algo(self, input_state):
        items = []

        for aglo in HashesOV:
            algo_value = aglo.value
            items.append(DropdownItem(algo_value))

        matches = [
            c
            for c in items
            if input_state.value.lower() in c.main.plain.lower()
        ]
        if matches == []:
            matches = items
        ordered = sorted(
            matches,
            key=lambda v: v.main.plain.startswith(input_state.value.lower()),
        )

        return ordered

    def compose(self) -> ComposeResult:
        yield Label("Create a new kill chain phase")
        yield self.source_name_field
        if self.source_name_field.content.lower() == "capec":
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
        yield self.description_field
        yield self.url_field

        if self.source_name_field.content.lower() == "capec":
            self.hashes_algo_field = AutoComplete(
                Input(placeholder="Enter the Hash Algorithm"),
                Dropdown(items=self.get_hashes_algo),
                title="Hash Algorithm",
                tab_moves_focus=True,
                id="hashes_algo_field",
                classes="hashes_fields",
                tooltip_text="""Specifies the algorithm of hash for the contents of the url.""",
            )

        yield Container(
            self.hashes_algo_field,
            self.hashes_value_field,
            id="horizontal-layout",
        )

    def on_mount(self):
        self.source_name_field.focus()

    def create_external_reference_form(self):
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
            title="External ID",
            placeholder="Enter the external id",
            title_align="left",
            auto_focus=True,
            required=True,
            tooltip_text="""An identifier for the external reference content.""",
        )

        self.description_field = CustomInputField(
            title="Description",
            placeholder="Enter the description",
            title_align="left",
            auto_focus=True,
            tooltip_text="""A human-readable description of the external reference.""",
        )

        self.url_field = CustomInputField(
            title="URL",
            placeholder="Enter the URL",
            title_align="left",
            auto_focus=True,
            tooltip_text="""A URL reference to an external resource [RFC3986].""",
        )

        self.hashes_algo_field = AutoComplete(
            Input(placeholder="Enter the Hash Algorithm"),
            Dropdown(items=self.get_hashes_algo),
            title="Hash Algorithm",
            tab_moves_focus=True,
            id="hashes_algo_field",
            classes="hashes_fields",
            tooltip_text="""Specifies the algorithm of hash for the contents of the url.""",
        )

        self.hashes_value_field = CustomInputField(
            title="Hash",
            placeholder="Enter the hash",
            title_align="left",
            auto_focus=False,
            id="hashes_value_field",
            classes="hashes_fields",
            tooltip_text="""Specifies the value of the hash for the contents of the url.""",
        )

    async def submit_execute(self):
        """Validate inputs and execute the creation of the kill chain phase."""
        error = await self.validate_external_reference()
        if error is None and self.hashes_value_field.has_focus:
            hashes = {}
            if (
                self.hashes_algo_field.input.value != ""
                and self.hashes_value_field.content != ""
            ):
                hashes = {
                    f"{self.hashes_algo_field.input.value}": f"{self.hashes_value_field.content}"
                }

            external_id_content = ""
            if isinstance(self.external_id_field, CustomInputField):
                external_id_content = self.external_id_field.content
            else:
                external_id_content = self.external_id_field.input.value

            await self.create_external_reference(
                source_name=self.source_name_field.content,
                external_id=external_id_content,
                description=self.description_field.content,
                url=self.url_field.content,
                hashes=hashes,
            )

    async def validate_external_reference(self):
        """Validate the kill chain and external ids."""
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

        if self.hashes_algo_field.input.value != "":
            if not HashesOV.from_value(self.hashes_algo_field.input.value):
                await self._load_error(
                    "Hash algorithm must be a known algorithm",
                    self.hashes_algo_field,
                    "hashes_algo_error",
                )
                return False

        return None

    async def on_key(self, event):
        """Handle key events and trigger submission on Enter key."""
        if event.key == "enter" or event.key == "tab":
            if event.key == "tab" and self.hashes_value_field.has_focus:
                event.stop()
            else:
                await self.submit_execute()

    async def create_external_reference(
        self,
        source_name: str,
        external_id: str,
        description: str,
        url: str,
        hashes: dict[str, str],
    ):
        """Create the kill chain phase and handle the result."""

        inputs = {
            "source_name": source_name,
            "external_id": external_id,
            "description": description,
            "url": url,
            "hashes": hashes,
        }
        await self.remove_errors()

        contract = CreateExternalReferenceAdapter.execute(
            inputs, STORAGE_ENGINE
        )

        if contract.error:
            await self._load_error(
                contract.error,
                self.source_name_field,
                id="error_duplicate",
            )
        else:
            await self.app.screen.action_clear_stat()
            self.app.screen._load_data_for_stix("External Reference")
            if contract.source_name.lower() == "capec":
                self.app.screen.navigation_tree.find_child(
                    f"{contract.source_name.lower()} - {ExternalReferenceCapec.from_id(contract.external_id.split("CAPEC-")[1]).name}"
                )
            else:
                self.app.screen.navigation_tree.find_child(
                    f"{contract.source_name} - {contract.external_id}"
                )
            self.app.simulate_key("r")

    async def remove_errors(self):
        """Remove error widgets from the form."""
        for error_id in [
            "source_name_error",
            "external_id_error",
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
