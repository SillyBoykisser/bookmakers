from typing import Optional
from sqlite3 import Connection, Cursor
import sqlite3

from bookmakers_office.interfaces.data_base_interfaces.data_base_connection_manager_interface import IDataBaseConnectionManager


class DataBaseConnectioManager(IDataBaseConnectionManager):
    def __init__(self, data_base_path: str):
        self.__db_path: str = data_base_path
        self.__connection: Optional[Connection] = None

    def connect(self) -> None:
        if self.__connection is None:
            self.__connection = sqlite3.connect(self.__db_path)
        else:
            raise ValueError("Database connection is already established")

    def execute(self, query: str) -> Cursor:
        print(query)
        if self.__connection is None:
            raise ValueError("Database connection is not established")
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor

    def commit(self) -> None:
        if self.__connection:
            self.__connection.commit()
        else:
            raise ValueError("Database connection is not established")

    def close(self) -> None:
        if self.__connection:
            self.__connection.close()
            self.__connection = None
        else:
            raise ValueError("Database connection is not established")
