from pytest import mark

from textual.css.query import NoMatches
from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

STORAGE_ENGINE = "INFILE"


@mark.order()
@mark.asyncio
async def test_access_new_projects_path():
    projects_path = "/tmp/GenStix/PyTests/New"

    ifr = InFilePersist()
    ifr.save_path = projects_path

    app = LaunchTUI(ifr.save_path)
    async with app.run_test() as pilot:
        await pilot.press("enter")
        try:
            app.screen.get_widget_by_id("Modal")
            assert True
        except NoMatches:
            assert False
