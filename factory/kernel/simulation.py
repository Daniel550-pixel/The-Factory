from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy
from typing import Any, Callable

@dataclass(frozen=True)
class SimulationResult:
    scenario: str
    state: dict[str, Any]

class SimulationEngine:
    def run(self, scenario: str, state: dict[str, Any], transition: Callable[[dict[str, Any]], dict[str, Any]]) -> SimulationResult:
        simulated = transition(deepcopy(state))
        return SimulationResult(scenario, simulated)
