from abc import ABC, abstractmethod
from bookmakers_office.table_schemes.basic_scheme import BasicScheme


class IDataBaseSchemeManager(ABC):
    @abstractmethod
    def generate_create_table_query(self) -> str:
        pass

    @abstractmethod
    def generate_crate_line_query(self, new_line: BasicScheme) -> str:
        pass
