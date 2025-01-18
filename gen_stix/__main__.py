from sys import exit

from gen_stix.src.app.cli.view.launch_cli import LaunchCLI
from gen_stix.src.app.tui.launch_tui import LaunchTUI
from gen_stix.src.app.repository.infile.infile_persist import InFilePersist


import logging

logging.basicConfig(
    filename="genstix.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def gen_stix():
    """The main entry point for the application."""

    if "--tui" in __import__("sys").argv:
        ifr = InFilePersist()
        app = LaunchTUI(ifr.save_path)
        app.run()
    else:
        app = LaunchCLI()
        app.start()


if __name__ == "__main__":
    try:
        exit(gen_stix())
    except Exception as e:
        logging.error(f"Exception occurred: {e}", exc_info=True)
        exit(1)
