from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any

class WorkerPool:
    def __init__(self, max_workers: int = 4) -> None:
        if max_workers < 1:
            raise ValueError("max_workers must be positive")
        self._pool = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, task: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        return self._pool.submit(task, *args, **kwargs)

    def shutdown(self) -> None:
        self._pool.shutdown(wait=True)
