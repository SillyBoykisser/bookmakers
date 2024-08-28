from bookmakers_office.interfaces.data_base_interfaces.data_base_table_manager_interface import IDataBaseTableManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_scheme_manager_interface import IDataBaseSchemeManager
from bookmakers_office.interfaces.data_base_interfaces.data_base_connection_manager_interface import IDataBaseConnectionManager
from bookmakers_office.models.table_model import Table


class DataBaseTableManager(IDataBaseTableManager):
    def __init__(self, table: Table, data_base: IDataBaseConnectionManager, scheme_manager: IDataBaseSchemeManager):
        self.__table: Table = table
        self.__db: IDataBaseConnectionManager = data_base
        self.scheme_manager: IDataBaseSchemeManager = scheme_manager

    def create_table(self) -> None:
        create_table_query = self.scheme_manager.generate_create_table_query()

        self.__db.connect()
        self.__db.execute(create_table_query)
        self.__db.commit()
        self.__db.close()

    def drop_table(self) -> None:
        drop_table_query = f"DROP TABLE {self.__table.table_name};"

        self.__db.connect()
        self.__db.execute(drop_table_query)
        self.__db.commit()
        self.__db.close()

