from __future__ import annotations
from enum import Enum


class PrintJobProcessingState(Enum):
	unknown = "unknown"
	pending = "pending"
	processing = "processing"
	paused = "paused"
	stopped = "stopped"
	completed = "completed"
	canceled = "canceled"
	aborted = "aborted"
	unknownFutureValue = "unknownFutureValue"

