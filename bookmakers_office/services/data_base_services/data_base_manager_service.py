from typing import Optional

from bookmakers_office.table_schemes.basic_scheme import BasicScheme
from bookmakers_office.interfaces.data_base_interfaces.data_base_manager_interface import IDataBaseManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_connection_manager_interface import IDataBaseConnectionManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_table_manager_interface import IDataBaseTableManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_crud_manager_interface import IDataBaseCRUDManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_scheme_manager_interface import IDataBaseSchemeManager
from bookmakers_office.services.data_base_services.data_base_connection_manager_service import DataBaseConnectioManager
from bookmakers_office.repositories.data_base_repositories.data_base_table_manager_repository import DataBaseTableManager
from bookmakers_office.repositories.data_base_repositories.data_base_crud_manager_repository import DataBaseCRUDManager
from bookmakers_office.services.data_base_services.data_base_sheme_manager_service import DataBaseSchemeManager
from bookmakers_office.models.table_model import Table


class DataBaseManager(IDataBaseManager):
    def __init__(self, data_base_path: str, table: Table):
        self.data_base_path: str = data_base_path
        self.table: Table = table

        self.__scheme_manager: IDataBaseSchemeManager = DataBaseSchemeManager(self.table)
        self.__db: IDataBaseConnectionManager = DataBaseConnectioManager(self.data_base_path)
        self.__db_table_manager: IDataBaseTableManager = DataBaseTableManager(self.table, self.__db, self.__scheme_manager)
        self.__db_crud_manager: IDataBaseCRUDManager = DataBaseCRUDManager(self.table, self.__db, self.__scheme_manager)

    def create_table(self) -> None:
        self.__db_table_manager.create_table()

    def drop_table(self) -> None:
        self.__db_table_manager.drop_table()

    def select(self, requirements: Optional[str] = None) -> tuple[tuple]:
        return self.__db_crud_manager.select(requirements)

    def insert(self, new_line: BasicScheme) -> None:
        self.__db_crud_manager.insert(new_line)

    def update(self, field_name: str, field_value: Optional[int | str | float | bool], requirements: str) -> None:
        self.__db_crud_manager.update(field_name, field_value, requirements)

    def delete(self, requirements: str) -> None:
        self.__db_crud_manager.delete(requirements)
