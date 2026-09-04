from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str

class TenantGuard:
    @staticmethod
    def owns(context: TenantContext, resource_tenant_id: str) -> bool:
        return context.tenant_id == resource_tenant_id
