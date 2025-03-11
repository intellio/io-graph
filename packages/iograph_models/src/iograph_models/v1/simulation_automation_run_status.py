from __future__ import annotations
from enum import StrEnum


class SimulationAutomationRunStatus(StrEnum):
	unknown = "unknown"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	skipped = "skipped"
	unknownFutureValue = "unknownFutureValue"

