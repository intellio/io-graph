from __future__ import annotations
from enum import StrEnum


class DocumentProcessingJobStatus(StrEnum):
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

