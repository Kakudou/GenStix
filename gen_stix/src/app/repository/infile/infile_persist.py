from dataclasses import dataclass
from os import path as os_path
from os.path import isfile as path_isfile
from yaml import safe_load as yaml_safe_load

from gen_stix.src.utils.singleton import Singleton
from gen_stix.src import SAVE_PATH


@Singleton
@dataclass
class InFilePersist:
    """This class is the in file storage system"""

    __save_path: str = SAVE_PATH

    @property
    def save_path(self) -> str:
        return self.__save_path

    @save_path.setter
    def save_path(self, save_path: str):
        self.__save_path = save_path


config_file = f"{os_path.dirname(os_path.abspath(__file__)).split('/GenSTIX/')[0]}/GenSTIX/.config.yml"
if path_isfile(config_file):
    with open(config_file, "r") as config:
        config = yaml_safe_load(config)
        ifr = InFilePersist()
        ifr.save_path = config["projects_path"]
