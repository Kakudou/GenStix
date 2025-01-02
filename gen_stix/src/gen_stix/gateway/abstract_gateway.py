from abc\
    import ABC, abstractmethod
from typing\
    import List


class AbstractGateway(ABC):

    @abstractmethod
    def _generate_id(self, identifier) -> str:
        raise NotImplementedError

    @abstractmethod
    def save(self, object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def exist_by_identifier(self, identifier) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update_by_identifier(self, identifier, object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def find_by_identifier(self, identifier) -> object:
        raise NotImplementedError

    @abstractmethod
    def destroy_by_identifier(self, identifier) -> bool:
        raise NotImplementedError
