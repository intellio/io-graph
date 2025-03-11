from __future__ import annotations
from enum import StrEnum


class PrintTaskProcessingState(StrEnum):
	pending = "pending"
	processing = "processing"
	completed = "completed"
	aborted = "aborted"
	unknownFutureValue = "unknownFutureValue"

