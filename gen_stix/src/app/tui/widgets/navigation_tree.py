from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Tree


class NavigationTree(Widget):

    def __init__(self, projects_path, id="navigation_tree") -> None:
        super().__init__(id=id)
        self.projects_path = projects_path
        self.current_node = None
        self.nav_tree = self.generate_nav_tree()
        self.nav_tree.center_scroll = True

    def compose(self) -> ComposeResult:
        yield self.nav_tree

    def generate_nav_tree(self):
        nav_tree: Tree[dict] = Tree(f"GenSTIX ({self.projects_path})")
        nav_tree.root.expand()
        return nav_tree

    def add_root(self, key, expand=False):
        self.nav_tree.root.add(key, expand=expand)
        self.nav_tree.refresh()

    def clear_tree(self):
        self.nav_tree.root._children = []
        self.nav_tree.refresh()

    def expand_root(self):
        self.nav_tree.root.expand()
        print("expand_root")
        print(self.nav_tree.root)
        self.nav_tree.refresh()

    def clear_root_children(self, root):
        def recursive(childs, root):
            for child in childs:
                if child.label.plain == root:
                    child._children = []
                    child.collapse()
                    return
                recursive(child.children, root)

        recursive(self.nav_tree.root.children, root)

    def add_sub_root(self, root, key):
        def recursive(childs, root, key):
            for child in childs:
                if child.label.plain == root:
                    child.add(key, expand=False)
                    return
                recursive(child.children, root, key)

        recursive(self.nav_tree.root.children, root, key)

    def add_leaf(self, root, key, value):
        def recursive(childs, root, key, value):
            for child in childs:
                if child.label.plain == root:
                    child.add_leaf(key, value)
                    return
                recursive(child.children, root, key, value)

        recursive(self.nav_tree.root.children, root, key, value)

    def add_bundle_leaf(self, root, bundles):
        for item in bundles:
            self.add_leaf(root, item, item)

    async def on_tree_node_highlighted(
        self, event: Tree.NodeHighlighted
    ) -> None:
        self.current_node = event.node
