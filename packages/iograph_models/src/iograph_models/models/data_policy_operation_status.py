from __future__ import annotations
from enum import StrEnum


class DataPolicyOperationStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	complete = "complete"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

