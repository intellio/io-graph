from __future__ import annotations
from enum import StrEnum


class ManagedAppLogUploadState(StrEnum):
	pending = "pending"
	inProgress = "inProgress"
	completed = "completed"
	declinedByUser = "declinedByUser"
	timedOut = "timedOut"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

