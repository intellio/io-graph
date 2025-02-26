from __future__ import annotations
from enum import Enum


class PrintTaskProcessingState(Enum):
	pending = "pending"
	processing = "processing"
	completed = "completed"
	aborted = "aborted"
	unknownFutureValue = "unknownFutureValue"

