from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Identity:
    subject: str
    roles: tuple[str, ...] = ()

class Authorizer:
    def __init__(self, role_capabilities: dict[str, set[str]] | None = None) -> None:
        self._roles = role_capabilities or {}

    def allowed(self, identity: Identity, capability: str) -> bool:
        return any(capability in self._roles.get(role, set()) for role in identity.roles)
