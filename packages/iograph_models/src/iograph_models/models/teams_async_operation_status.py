from __future__ import annotations
from enum import StrEnum


class TeamsAsyncOperationStatus(StrEnum):
	invalid = "invalid"
	notStarted = "notStarted"
	inProgress = "inProgress"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

