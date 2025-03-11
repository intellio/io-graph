from __future__ import annotations
from enum import StrEnum


class IndustryDataIndustryDataActivityStatus(StrEnum):
	inProgress = "inProgress"
	skipped = "skipped"
	failed = "failed"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	completedWithWarnings = "completedWithWarnings"
	unknownFutureValue = "unknownFutureValue"

