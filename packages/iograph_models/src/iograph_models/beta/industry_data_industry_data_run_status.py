from __future__ import annotations
from enum import StrEnum


class IndustryDataIndustryDataRunStatus(StrEnum):
	running = "running"
	failed = "failed"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	completedWithWarnings = "completedWithWarnings"
	unknownFutureValue = "unknownFutureValue"

