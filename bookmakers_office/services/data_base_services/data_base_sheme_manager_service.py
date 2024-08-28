from dataclasses import fields, asdict
from typing import Type

from bookmakers_office.interfaces.data_base_interfaces.data_base_scheme_manager_interface import IDataBaseSchemeManager
from bookmakers_office.models.table_model import Table
from bookmakers_office.table_schemes.basic_scheme import BasicScheme


class DataBaseSchemeManager(IDataBaseSchemeManager):
    def __init__(self, table: Table):
        self.__table_name = table.table_name
        self.__scheme: Type[BasicScheme] = table.scheme

    def generate_create_table_query(self) -> str:
        fields_names = [field.name for field in fields(self.__scheme)]
        fields_types = [field.type for field in fields(self.__scheme)]
        fields_sql_types = [self.__get_sql_type(field_type) for field_type in fields_types]
        fields_dict = {field_name: field_type for (field_name, field_type) in zip(fields_names, fields_sql_types)}

        query = f'CREATE TABLE IF NOT EXISTS {self.__table_name} ('
        for key, value in fields_dict.items():
            query += f'{key} {value},'
        query = query[:-1]
        query += ')'

        return query

    def generate_crate_line_query(self, new_line: BasicScheme) -> str:
        if type(new_line) is not self.__scheme:
            raise TypeError(f"Expected instance of {self.__scheme.__name__}, got {type(new_line).__name__}")

        line_dict = asdict(new_line)

        query = f'INSERT INTO {self.__table_name} ('
        query_key = ''
        query_value = ''
        for key, value in line_dict.items():
            query_value += f"{value}, "
            query_key += f'{key}, '
        query_key = query_key[:-2]
        query_value = query_value[:-2]
        query = query + query_key + ')' + ' VALUES ' + '(' + query_value + ');'

        return query

    @staticmethod
    def __get_sql_type(python_type: type) -> str:
        if python_type is str:
            sql_type = "TEXT"
        elif python_type is int:
            sql_type = "INTEGER"
        elif python_type is float:
            sql_type = "REAL"
        elif python_type is bool:
            sql_type = "BOOLEAN"
        else:
            raise ValueError("No such type in database")
        return sql_type

