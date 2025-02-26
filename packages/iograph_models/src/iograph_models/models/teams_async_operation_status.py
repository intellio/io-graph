from __future__ import annotations
from enum import Enum


class TeamsAsyncOperationStatus(Enum):
	invalid = "invalid"
	notStarted = "notStarted"
	inProgress = "inProgress"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

