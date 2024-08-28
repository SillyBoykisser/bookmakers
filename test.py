from dataclasses import dataclass, fields
from abc import ABC, abstractmethod
from typing import Type
from enum import Enum, auto
from dataclasses import dataclass, field, fields
from typing import Any





@dataclass
class BasicScheme:
    id: int
    name: str







class Smth:
    def __init__(self, table: Type[BasicScheme]):
        self.table = table
        self.create_enum()

    def create_enum(self):
        # Динамическое создание перечисления из полей датакласса
        enum_members = {field.name: auto() for field in fields(self.table)}
        self.Field = Enum('Field', enum_members)

    def func(self):
        print(self.Field.age)

def dataclass_with_enum(cls):
    """Декоратор для создания перечисления на основе полей датакласса"""
    enum_members = {field.name: auto() for field in fields(cls)}
    return Enum('Fields', enum_members)


@dataclass_with_enum
@dataclass
class ExampleDataClass:
    name: str
    age: int
    gender: str

    @property
    def field(cls):
        """Декоратор для создания перечисления на основе полей датакласса"""
        enum_members = {field.name: auto() for field in fields(cls)}
        return Enum('Fields', enum_members)


print(ExampleDataClass.field.name)


