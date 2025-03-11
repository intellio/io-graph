from __future__ import annotations
from enum import StrEnum


class SimulationAutomationStatus(StrEnum):
	unknown = "unknown"
	draft = "draft"
	notRunning = "notRunning"
	running = "running"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"

