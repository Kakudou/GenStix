from pytest import mark

from textual.css.query import NoMatches
from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

STORAGE_ENGINE = "INFILE"


@mark.order()
@mark.asyncio
async def test_delete_all_external_reference():
    projects_path = "/tmp/GenStix/PyTests"
    project_name = "DeleteAllExternalReference"

    ifr = InFilePersist()
    ifr.save_path = projects_path
    app = LaunchTUI(ifr.save_path)
    async with app.run_test() as pilot:
        await pilot.press("enter")
        try:
            app.screen.get_widget_by_id("Modal")
            await pilot.press("enter")
        except NoMatches:
            pass
        assert app.title == "GenSTIX - Home Screen"
        await pilot.press("c")
        await pilot.press(*project_name)
        await pilot.press("enter")
        await pilot.press("enter")
        await pilot.press("enter")
        app.screen.navigation_tree.find_child("CDTs")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == "CDTs"
        await pilot.press("enter")
        app.screen.navigation_tree.find_child("External Reference")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == "External Reference"
        await pilot.press("c")
        source_name = "pytest-tui-source"
        await pilot.press(*source_name)
        await pilot.press("enter")
        external_id = "pytest-tui-external-id"
        await pilot.press(*external_id)
        await pilot.press("enter")
        description = "pytest-tui-description"
        await pilot.press(*description)
        await pilot.press("enter")
        url = "pytest-tui-url"
        await pilot.press(*url)
        await pilot.press("enter")
        app.screen.navigation_tree.find_child(f"{source_name} - {external_id}")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == f"{source_name} - {external_id}"
        app.screen.navigation_tree.find_child("External Reference")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == "External Reference"
        await pilot.press("c")
        source_name = "pytest-tui-source2"
        await pilot.press(*source_name)
        await pilot.press("enter")
        external_id = "pytest-tui-external-id2"
        await pilot.press(*external_id)
        await pilot.press("enter")
        description = "pytest-tui-description2"
        await pilot.press(*description)
        await pilot.press("enter")
        url = "pytest-tui-url2"
        await pilot.press(*url)
        await pilot.press("enter")
        app.screen.navigation_tree.find_child(f"{source_name} - {external_id}")
        current_node = app.screen.navigation_tree.current_node
        app.screen.navigation_tree.find_child("External Reference")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == "External Reference"
        await pilot.press("enter")
        nb_childs_before = len(current_node._children)
        await pilot.press("d")
        await pilot.press(*"yes")
        await pilot.press("enter")
        app.screen.navigation_tree.find_child("External Reference")
        current_node = app.screen.navigation_tree.current_node
        nb_childs_after = len(current_node._children)
        assert nb_childs_before != nb_childs_after
        assert nb_childs_after == 0
