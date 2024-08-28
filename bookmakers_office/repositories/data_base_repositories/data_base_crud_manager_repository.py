from typing import Optional


from bookmakers_office.interfaces.data_base_interfaces.data_base_connection_manager_interface import IDataBaseConnectionManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_crud_manager_interface import IDataBaseCRUDManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_scheme_manager_interface import IDataBaseSchemeManager
from bookmakers_office.models.table_model import Table
from bookmakers_office.table_schemes.basic_scheme import BasicScheme


class DataBaseCRUDManager(IDataBaseCRUDManager):
    def __init__(self, table: Table, data_base: IDataBaseConnectionManager, scheme_manager: IDataBaseSchemeManager):
        self.__table: Table = table
        self.__db: IDataBaseConnectionManager = data_base
        self.scheme_manager: IDataBaseSchemeManager = scheme_manager

    def select(self, requirements: Optional[str] = None) -> tuple[tuple]:
        if requirements is None:
            query = f'SELECT * FROM {self.__table.table_name}'
        else:
            query = f'SELECT * FROM {self.__table.table_name} WHERE {requirements}'

        self.__db.connect()
        cursor = self.__db.execute(query)
        self.__db.commit()
        result = tuple(cursor.fetchall())
        self.__db.close()

        return result

    def insert(self, new_line: BasicScheme) -> None:

        query = self.scheme_manager.generate_crate_line_query(new_line)

        self.__db.connect()
        self.__db.execute(query)
        self.__db.commit()
        self.__db.close()

    def update(self, field_name: str, field_value: Optional[int| str| float | bool], requirements: str) -> None:
        query = f"UPDATE {self.__table.table_name} SET {field_name} = {field_value} WHERE {requirements}"

        self.__db.connect()
        self.__db.execute(query)
        self.__db.commit()
        self.__db.close()

    def delete(self, requirements: str) -> None:
        query = f'DELETE FROM {self.__table.table_name} WHERE {requirements}'

        self.__db.connect()
        self.__db.execute(query)
        self.__db.commit()
        self.__db.close()
