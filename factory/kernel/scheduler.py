from __future__ import annotations
from dataclasses import dataclass
from queue import Queue
from typing import Callable

@dataclass(frozen=True)
class Task:
    task_id: str
    name: str

class Scheduler:
    def __init__(self) -> None:
        self._queue: Queue[Task] = Queue()
        self._handlers: dict[str, Callable[[], None]] = {}

    def register(self, name: str, handler: Callable[[], None]) -> None:
        self._handlers[name] = handler

    def submit(self, task: Task) -> None:
        self._queue.put(task)

    def run_once(self) -> Task | None:
        if self._queue.empty():
            return None
        task = self._queue.get()
        handler = self._handlers.get(task.name)
        if handler is None:
            raise KeyError(f"no handler for task: {task.name}")
        handler()
        return task
