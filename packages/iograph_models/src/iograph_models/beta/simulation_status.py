from __future__ import annotations
from enum import StrEnum


class SimulationStatus(StrEnum):
	unknown = "unknown"
	draft = "draft"
	running = "running"
	scheduled = "scheduled"
	succeeded = "succeeded"
	failed = "failed"
	cancelled = "cancelled"
	excluded = "excluded"
	unknownFutureValue = "unknownFutureValue"

