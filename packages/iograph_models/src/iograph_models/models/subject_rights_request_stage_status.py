from __future__ import annotations
from enum import StrEnum


class SubjectRightsRequestStageStatus(StrEnum):
	notStarted = "notStarted"
	current = "current"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

