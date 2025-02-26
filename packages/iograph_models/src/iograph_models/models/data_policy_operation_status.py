from __future__ import annotations
from enum import Enum


class DataPolicyOperationStatus(Enum):
	notStarted = "notStarted"
	running = "running"
	complete = "complete"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

