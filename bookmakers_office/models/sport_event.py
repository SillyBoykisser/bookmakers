from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    name: str
    date: str
    time: str
    participants: dict
    coefficients: dict[str, float]
    has_started: bool
    has_ended: bool
