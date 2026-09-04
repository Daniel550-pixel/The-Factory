from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class APIRequest:
    operation: str
    payload: dict[str, Any]

@dataclass(frozen=True)
class APIResponse:
    ok: bool
    payload: dict[str, Any]

class FactoryAPI:
    def __init__(self) -> None:
        self._handlers: dict[str, Any] = {}

    def register(self, operation: str, handler: Any) -> None:
        self._handlers[operation] = handler

    def handle(self, request: APIRequest) -> APIResponse:
        if request.operation not in self._handlers:
            return APIResponse(False, {"error": "unknown operation"})
        return APIResponse(True, {"result": self._handlers[request.operation](request.payload)})
