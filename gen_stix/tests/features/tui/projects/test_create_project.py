from pytest import mark

from textual.css.query import NoMatches
from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

STORAGE_ENGINE = "INFILE"


@mark.order()
@mark.asyncio
async def test_create_project():
    projects_path = "/tmp/GenStix/PyTests"
    project_name = "CreateProject"

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
        app.screen.navigation_tree.focus_child(project_name)
        entry = app.screen.navigation_tree.current_node.label.plain
        await pilot.press("enter")
        app.screen.navigation_tree.find_child(project_name)
        next_entry = app.screen.navigation_tree.current_node.label.plain
        assert next_entry == entry

        for key in ["SDOs", "SCOs", "SROs", "CDTs"]:
            await pilot.press("enter")
            app.screen.navigation_tree.find_child(key)
            next_entry = app.screen.navigation_tree.current_node.label.plain
            assert next_entry == key
