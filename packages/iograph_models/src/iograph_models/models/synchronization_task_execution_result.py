from __future__ import annotations
from enum import StrEnum


class SynchronizationTaskExecutionResult(StrEnum):
	Succeeded = "Succeeded"
	Failed = "Failed"
	EntryLevelErrors = "EntryLevelErrors"

