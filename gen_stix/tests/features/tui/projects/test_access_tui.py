from shutil import rmtree
from pytest import mark

from gen_stix.src.app.tui.launch_tui import LaunchTUI

from gen_stix.src.app.repository.infile.infile_persist import InFilePersist

STORAGE_ENGINE = "INFILE"


@mark.order(0)
@mark.asyncio
async def test_access_tui():
    projects_path = "/tmp/GenStix/PyTests"
    rmtree(projects_path, ignore_errors=True)

    ifr = InFilePersist()
    ifr.save_path = projects_path

    app = LaunchTUI(ifr.save_path)
    async with app.run_test():
        assert app.title == "GenSTIX TUI - Start Screen"
        for w in app.screen._dirty_widgets:
            if w.__str__() == "CustomInputField()":
                assert w.content == projects_path
