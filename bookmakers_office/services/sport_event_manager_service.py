from typing import Type

from bookmakers_office.interfaces.sport_event_manager_interface import ISportEventManager
from bookmakers_office.models.sport_event import BasicSportEvent


class SportEventManager(ISportEventManager):
    events = {}

    def add_event(self, event: Type[BasicSportEvent], **event_data):
        pass

    def delete_event(self, event: BasicSportEvent):
        pass

    def start_event(self, event: BasicSportEvent):
        pass

    def end_event(self, event: BasicSportEvent):
        pass
