from __future__ import annotations
from enum import StrEnum


class SecurityLongRunningOperationStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	skipped = "skipped"
	unknownFutureValue = "unknownFutureValue"

