from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass(frozen=True)
class TelemetryRecord:
    name: str
    trace_id: str | None = None
    attributes: dict[str, Any] = field(default_factory=dict)

class Telemetry:
    def __init__(self) -> None:
        self._sinks: list[Callable[[TelemetryRecord], None]] = []

    def add_sink(self, sink: Callable[[TelemetryRecord], None]) -> None:
        self._sinks.append(sink)

    def emit(self, record: TelemetryRecord) -> None:
        for sink in tuple(self._sinks):
            try:
                sink(record)
            except Exception:
                continue
