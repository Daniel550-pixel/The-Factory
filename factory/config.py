from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class FactoryConfig:
    environment: str = "development"
    database_url: str | None = None
    telemetry_endpoint: str | None = None

    @classmethod
    def from_environment(cls) -> "FactoryConfig":
        return cls(
            environment=os.getenv("FACTORY_ENV", "development"),
            database_url=os.getenv("FACTORY_DATABASE_URL"),
            telemetry_endpoint=os.getenv("FACTORY_TELEMETRY_ENDPOINT"),
        )
