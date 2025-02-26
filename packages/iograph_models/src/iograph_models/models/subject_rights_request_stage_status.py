from __future__ import annotations
from enum import Enum


class SubjectRightsRequestStageStatus(Enum):
	notStarted = "notStarted"
	current = "current"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

