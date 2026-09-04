from __future__ import annotations
from typing import Any
from .kernel.events import Event

class EventRepository:
    """Storage seam; database implementations can satisfy this contract later."""
    def append(self, event: Event) -> None:
        raise NotImplementedError

    def load(self) -> tuple[Event, ...]:
        raise NotImplementedError

class MemoryEventRepository(EventRepository):
    def __init__(self) -> None:
        self._events: list[Event] = []

    def append(self, event: Event) -> None:
        self._events.append(event)

    def load(self) -> tuple[Event, ...]:
        return tuple(self._events)
