from __future__ import annotations
from enum import StrEnum


class PrintJobProcessingState(StrEnum):
	unknown = "unknown"
	pending = "pending"
	processing = "processing"
	paused = "paused"
	stopped = "stopped"
	completed = "completed"
	canceled = "canceled"
	aborted = "aborted"
	unknownFutureValue = "unknownFutureValue"

