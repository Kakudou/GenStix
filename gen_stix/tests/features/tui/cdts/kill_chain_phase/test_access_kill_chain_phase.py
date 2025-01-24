from pytest import mark

from textual.css.query import NoMatches
from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

STORAGE_ENGINE = "INFILE"


@mark.order()
@mark.asyncio
async def test_access_kill_chain_phase():
    projects_path = "/tmp/GenStix/PyTests"
    project_name = "AccessKillChainPhase"

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
        app.screen.navigation_tree.find_child("Kill Chain Phase")
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == "Kill Chain Phase"
        await pilot.press("c")
        kill_chain_name = "pytest-tui-kill-chain"
        phase_name = "pytest-tui-phase"
        await pilot.press(*kill_chain_name)
        await pilot.press("enter")
        await pilot.press(*phase_name)
        await pilot.press("enter")
        app.screen.navigation_tree.find_child(
            f"{kill_chain_name} - {phase_name}"
        )
        current_node = app.screen.navigation_tree.current_node
        assert current_node.label.plain == f"{kill_chain_name} - {phase_name}"
        await pilot.press("r")
        widget = app.screen.get_widget_by_id("ContentScreen")
        found = False
        for child in widget.children:
            if str(child) == "Markdown()":
                found = True
                break

        assert found
