from abc import ABC, abstractmethod
from typing import Optional

from bookmakers_office.table_schemes.basic_scheme import BasicScheme


class IDataBaseManager(ABC):
    @abstractmethod
    def create_table(self) -> None:
        pass

    @abstractmethod
    def drop_table(self) -> None:
        pass

    @abstractmethod
    def select(self, requirements: Optional[str] = None) -> tuple[tuple]:
        pass

    @abstractmethod
    def insert(self, new_line: BasicScheme) -> None:
        pass

    @abstractmethod
    def update(self, field_name: str, field_value: Optional[int | str | float | bool], requirements: str) -> None:
        pass

    @abstractmethod
    def delete(self, requirements: str) -> None:
        pass
