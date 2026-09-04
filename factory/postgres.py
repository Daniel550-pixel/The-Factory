from __future__ import annotations
from typing import Any
from .kernel.events import Event

SCHEMA = """CREATE TABLE IF NOT EXISTS factory_events (sequence BIGINT PRIMARY KEY, event_type TEXT NOT NULL, payload JSONB NOT NULL, timestamp TEXT NOT NULL, correlation_id TEXT, causation_id TEXT, previous_hash TEXT, event_hash TEXT NOT NULL UNIQUE);"""

class PostgresEventStore:
    """DB-API compatible adapter; install/configure a PostgreSQL driver at deployment time."""
    def __init__(self, connection: Any) -> None:
        self.connection = connection

    def initialize(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(SCHEMA)
        self.connection.commit()

    def append(self, event: Event) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO factory_events (sequence,event_type,payload,timestamp,correlation_id,causation_id,previous_hash,event_hash) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (event.sequence, event.event_type, event.payload, event.timestamp, event.correlation_id, event.causation_id, event.previous_hash, event.event_hash),
            )
        self.connection.commit()
