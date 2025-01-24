from textual.css.query import NoMatches
from gen_stix.src.app.tui.widgets.navigation_tree import NavigationTree
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tree
from textual import events
from textual.widgets import LoadingIndicator
from gen_stix.src.app import adapter as adapter
from gen_stix.src.app.repository.infile.infile_persist import InFilePersist
from gen_stix.src.app.tui.widgets.help_widget import HelpWidget


class HomeScreen(Screen):

    BINDINGS = [
        ("c", "create", "(C)reate"),
        ("a", "access", "(A)ccess"),
        ("u", "update", "(U)pdate"),
        ("d", "delete", "(D)elete"),
        ("f", "find", "(F)ind"),
        ("h", "help", "(H)elp"),
        ("q", "clear", "Clear The content screen"),
        ("ctrl+c", "quit", "Quit"),
        (
            "tab",
            "focus_next",
            "Switch focus from navigation to content screen",
        ),
    ]

    cdts = [
        "Kill Chain Phase",
        # ?         "External Reference",
        # ?         "Hashes",
    ]

    sdos = [
        # ?         "Attack Pattern",
        # ?         "Campaign",
        # ?         "Course of Action",
        # ?         "Identity",
        # ?         "Indicator",
        # ?         "Intrusion Set",
        # ?         "Location",
        # ?         "Malware Analysis",
        # ?         "Malware",
        # ?         "Note",
        # ?         "Observed Data",
        # ?         "Opinion",
        # ?         "Report",
        # ?         "Threat Actor",
        # ?         "Tool",
        # ?         "Vulnerability",
    ]

    sros = [
        # ?         "Relationship",
        # ?         "Sighting",
    ]

    scos = [
        # ?         "Artifact",
        # ?         "Autonomous System",
        # ?         "Directory",
        # ?         "Domain Name",
        # ?         "Email Address",
        # ?         "Email Message",
        # ?         "File",
        # ?         "IPv4 Address",
        # ?         "IPv6 Address",
        # ?         "MAC Address",
        # ?         "Mutex",
        # ?         "Network Traffic",
        # ?         "Process",
        # ?         "Software",
        # ?         "URL",
        # ?         "User Account",
        # ?         "Windows Registry Key",
        # ?         "X509 Certificate",
    ]

    def __init__(self) -> None:
        super().__init__()
        self.app.session["project"] = ""
        self.app.title = "GenSTIX - Home Screen"
        self.navigation_tree = NavigationTree(
            self.app.session["projects_path"], id="NavigationTree"
        )
        self.init_navigation_tree()

    def init_navigation_tree(self) -> None:
        try:
            with open(
                f"{self.app.session['projects_path']}/.projects", "r"
            ) as f:
                all_projects = f.read().splitlines()
                for project in all_projects:
                    self.navigation_tree.add_root(project, expand=False)
        except Exception:
            pass

    def reload_navigation_tree(self) -> None:
        self.navigation_tree.clear_tree()
        self.init_navigation_tree()
        self.navigation_tree.expand_root()

    def on_mount(self) -> None:
        self.query_one("Tree").focus()

    def compose(self) -> ComposeResult:
        yield Header()
        yield self.navigation_tree
        yield HelpWidget(id="ContentScreen", classes="ContentScreen")
        yield Footer()

    async def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        await self.on_tree_node_selected(event)

    async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        if event.node.parent and event.node.parent.label.plain.startswith(
            "GenSTIX ("
        ):
            project_name = event.node.label.plain
            self._load_project(project_name)

    def _load_project(self, project_name: str):
        """Handle loading project data into the navigation tree."""
        if self.app.session["project"] != project_name:
            self.navigation_tree.clear_root_children(
                self.app.session["project"]
            )
            self.app.session["project"] = project_name

            ifr = InFilePersist()
            ifr.save_path = (
                f"{self.app.session['projects_path']}/{project_name}"
            )

            # Load sub-roots and data dynamically
            # ?             self.navigation_tree.add_root(project_name, expand=False)
            self.navigation_tree.add_sub_root(project_name, "SDOs")
            self._load_data_for_project("SDOs")
            self.navigation_tree.add_sub_root(project_name, "SCOs")
            self._load_data_for_project("SCOs")
            self.navigation_tree.add_sub_root(project_name, "SROs")
            self._load_data_for_project("SROs")
            self.navigation_tree.add_sub_root(project_name, "CDTs")
            self._load_data_for_project("CDTs")

    def _load_data_for_project(self, data_type: str, expand=False) -> None:
        """Helper method to load data for project (SDOs, SCOs, SROs, CDTs)."""
        if data_type == "SDOs":
            data_list = self.sdos
        elif data_type == "SCOs":
            data_list = self.scos
        elif data_type == "SROs":
            data_list = self.sros
        elif data_type == "CDTs":
            data_list = self.cdts
        else:
            data_list = []

        for data in data_list:
            self.navigation_tree.clear_root_children(data_type)
            self.navigation_tree.add_sub_root(data_type, data, expand=expand)
            adapter_to_call = getattr(
                adapter, f"List{data.replace(' ', '')}Adapter"
            )
            return_object_attribute = f"all_{data.replace(' ', '_').lower()}s"
            contract = adapter_to_call.execute({})
            data_objects = getattr(contract, return_object_attribute)
            self.navigation_tree.add_bundle_leaf(data, data_objects)

    def _load_data_for_stix(self, data_type: str) -> None:
        """Helper method to load data for stix (Kill Chain Phase, External Reference, Hashes, ...)."""
        self.navigation_tree.clear_root_children(data_type)
        adapter_to_call = getattr(
            adapter, f"List{data_type.replace(' ', '')}Adapter"
        )
        return_object_attribute = f"all_{data_type.replace(' ', '_').lower()}s"
        contract = adapter_to_call.execute({})
        data_objects = getattr(contract, return_object_attribute)
        self.navigation_tree.add_bundle_leaf(data_type, data_objects)
        self.navigation_tree.focus_child(data_type)
        self.navigation_tree.current_node.expand()

    async def on_key(self, event: events.Key) -> None:
        key_action_map = {
            ("c", "C"): self.action_create_dyn,
            ("a", "r", "A", "R", "f", "F"): self.action_read_dyn,
            ("u", "U"): self.action_update_dyn,
            ("d", "D"): self.action_delete_dyn,
            ("h", "H"): self.action_help_stat,
            ("q", "Q", "escape"): self.action_clear_stat,
        }
        target = self.navigation_tree.current_node

        if event.key == "space" and self.navigation_tree.has_focus_within:
            if self.navigation_tree.current_node._children == []:
                self.navigation_tree.current_node.parent.toggle()

        for keys, action in key_action_map.items():
            if event.key in keys and event.key == "escape":
                await action()
                break
            elif event.key in keys and self.navigation_tree.has_focus_within:
                if event.key in ["q", "Q", "h", "H"]:
                    await action()
                    break
                await action(target)
                break

    async def clean_widgets(self) -> None:
        """Clean up existing widgets."""
        try:
            await self.get_widget_by_id("ContentScreen").remove()
        except NoMatches:
            pass
        try:
            await self.get_widget_by_id("loading").remove()
        except NoMatches:
            pass

    async def action_help_stat(self) -> None:
        await self.clean_widgets()
        self.mount(HelpWidget(id="ContentScreen", classes="ContentScreen"))

    async def action_clear_stat(self) -> None:
        await self.clean_widgets()
        self.mount(LoadingIndicator(id="loading", classes="ContentScreen"))

    async def action_create_dyn(
        self, node: Tree.NodeSelected | None = None
    ) -> None:
        if node:
            await self.clean_widgets()
            await self.load_widget_dyn(node, "Create")

    async def action_read_dyn(
        self, node: Tree.NodeSelected | None = None
    ) -> None:
        if node:
            await self.clean_widgets()
            await self.load_widget_dyn(node, "Read")

    async def action_update_dyn(
        self, node: Tree.NodeSelected | None = None
    ) -> None:
        if node:
            await self.clean_widgets()
            await self.load_widget_dyn(node, "Update")

    async def action_delete_dyn(
        self, node: Tree.NodeSelected | None = None
    ) -> None:
        if node:
            await self.clean_widgets()
            if node.label.plain.startswith("GenSTIX ("):
                await self.action_clear_stat()
            else:
                await self.load_widget_dyn(node, "Delete")

    async def load_widget_dyn(self, node, operation):
        widget_to_load, node_target = self.identify_widget_to_load(node)
        if widget_to_load:
            await self.clean_widgets()
            cat_stix = None
            if widget_to_load in self.sdos:
                cat_stix = "sdos."
            elif widget_to_load in self.sros:
                cat_stix = "sros."
            elif widget_to_load in self.scos:
                cat_stix = "scos."
            elif widget_to_load in self.cdts:
                cat_stix = "cdts."
            else:
                cat_stix = ""

            try:
                module = __import__(
                    f"gen_stix.src.app.tui.widgets.{cat_stix}{widget_to_load.replace(' ', '_').lower()}.{operation.lower()}_{widget_to_load.replace(' ', '_').lower()}_widget",
                    fromlist=[
                        f"{operation}{widget_to_load.replace(' ', '')}Widget"
                    ],
                )
                class_ = getattr(
                    module,
                    f"{operation}{widget_to_load.replace(' ', '')}Widget",
                )
                self.mount(
                    class_(
                        id="ContentScreen",
                        classes="ContentScreen",
                        target=node_target,
                    )
                )
            except ModuleNotFoundError:
                await self.action_clear_stat()

    def identify_widget_to_load(self, node: Tree.NodeSelected) -> tuple:
        """Identify the widget to load based on node properties."""
        node_label = node.label.plain
        node_parent_label = node.parent.label.plain if node.parent else ""
        all_objects = self.cdts + self.sdos + self.sros + self.scos
        widget_to_load = ""
        node_target = ""

        if node_label.startswith("GenSTIX ("):
            widget_to_load = "Project"
        elif node_parent_label.startswith("GenSTIX ("):
            widget_to_load = "Project"
            node_target = node
        elif node_label in all_objects:
            widget_to_load = f"{node_label}"
            node_target = node
        elif node_parent_label in all_objects:
            widget_to_load = f"{node_parent_label}"
            node_target = node

        return widget_to_load, node_target
