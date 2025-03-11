from __future__ import annotations
from enum import StrEnum


class RestoreArtifactsBulkRequestStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	unknownFutureValue = "unknownFutureValue"

