import os

from pytest import mark
from textual.css.query import NoMatches
from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist


STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@mark.asyncio
async def test_access_project_folder():
    ifr = InFilePersist()
    ifr.save_path = "/tmp/GenStix/PytTests"
    app = LaunchTUI(ifr.save_path)
    async with app.run_test() as pilot:
        assert app.title == "GenSTIX TUI - Start Screen"
        for w in app.screen._dirty_widgets:
            if w.__str__() == "CustomInputField()":
                assert w.content == ifr.save_path
                await pilot.press("enter")
                break
        try:
            app.screen.get_widget_by_id("Modal")
            await pilot.press("enter")
        except NoMatches:
            pass
        assert app.title == "GenSTIX - Home Screen"
