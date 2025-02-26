from __future__ import annotations
from enum import Enum


class SimulationStatus(Enum):
	unknown = "unknown"
	draft = "draft"
	running = "running"
	scheduled = "scheduled"
	succeeded = "succeeded"
	failed = "failed"
	cancelled = "cancelled"
	excluded = "excluded"
	unknownFutureValue = "unknownFutureValue"

