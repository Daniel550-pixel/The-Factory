from __future__ import annotations
from typing import Protocol
from .scheduler import Task

class TaskQueue(Protocol):
    def publish(self, task: Task) -> None: ...
    def consume(self) -> Task | None: ...

class LocalTaskQueue:
    def __init__(self) -> None:
        self._items: list[Task] = []

    def publish(self, task: Task) -> None:
        self._items.append(task)

    def consume(self) -> Task | None:
        return self._items.pop(0) if self._items else None
