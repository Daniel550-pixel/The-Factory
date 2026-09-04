from __future__ import annotations
from typing import Any

class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, Any] = {}

    def register(self, name: str, provider: Any) -> None:
        self._providers[name] = provider

    def get(self, name: str) -> Any:
        if name not in self._providers:
            raise KeyError(f"unknown provider: {name}")
        return self._providers[name]

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._providers))
