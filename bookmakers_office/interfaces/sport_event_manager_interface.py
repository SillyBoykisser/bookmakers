from abc import abstractmethod, ABC
from typing import Type

from bookmakers_office.models.sport_event import BasicSportEvent


class ISportEventManager(ABC):
    events = {}

    @abstractmethod
    def add_event(self, event: Type[BasicSportEvent], **event_data):
        pass

    @abstractmethod
    def delete_event(self, event: BasicSportEvent.event_id):
        pass

    @abstractmethod
    def start_event(self, event: BasicSportEvent.event_id):
        pass

    @abstractmethod
    def end_event(self, event: BasicSportEvent.event_id):
        pass
