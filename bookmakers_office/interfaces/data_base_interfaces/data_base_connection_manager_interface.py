from abc import ABC, abstractmethod
from typing import Optional


class IDataBaseConnectionManager(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute(self, query: str) -> Optional[tuple]:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
