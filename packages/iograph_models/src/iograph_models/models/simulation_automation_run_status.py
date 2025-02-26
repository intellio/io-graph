from __future__ import annotations
from enum import Enum


class SimulationAutomationRunStatus(Enum):
	unknown = "unknown"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	skipped = "skipped"
	unknownFutureValue = "unknownFutureValue"

