from __future__ import annotations
from enum import Enum


class LongRunningOperationStatus(Enum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

