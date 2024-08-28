from dataclasses import dataclass
from typing import Type

from bookmakers_office.table_schemes.basic_scheme import BasicScheme


@dataclass
class Table:
    table_name: str
    scheme: Type[BasicScheme]
