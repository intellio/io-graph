from __future__ import annotations
from enum import StrEnum


class PrinterProcessingState(StrEnum):
	unknown = "unknown"
	idle = "idle"
	processing = "processing"
	stopped = "stopped"
	unknownFutureValue = "unknownFutureValue"

