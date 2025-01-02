from dataclasses\
    import dataclass
from typing\
    import Dict

from gen_stix.src.utils.singleton\
    import Singleton


@Singleton
@dataclass
class InMemoryPersist:
    """This class is the in memory storage system"""

    __storage: Dict = None

    @property
    def storage(self) -> Dict:
        return self.__storage

    @storage.setter
    def storage(self, storage: Dict):
        self.__storage = storage
