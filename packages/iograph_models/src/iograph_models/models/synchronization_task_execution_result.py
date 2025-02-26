from __future__ import annotations
from enum import Enum


class SynchronizationTaskExecutionResult(Enum):
	Succeeded = "Succeeded"
	Failed = "Failed"
	EntryLevelErrors = "EntryLevelErrors"

