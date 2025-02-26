from __future__ import annotations
from enum import Enum


class PrinterProcessingState(Enum):
	unknown = "unknown"
	idle = "idle"
	processing = "processing"
	stopped = "stopped"
	unknownFutureValue = "unknownFutureValue"

