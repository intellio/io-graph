from __future__ import annotations
from enum import Enum


class SimulationAutomationStatus(Enum):
	unknown = "unknown"
	draft = "draft"
	notRunning = "notRunning"
	running = "running"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"

