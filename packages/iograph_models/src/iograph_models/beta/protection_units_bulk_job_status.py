from __future__ import annotations
from enum import StrEnum


class ProtectionUnitsBulkJobStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	unknownFutureValue = "unknownFutureValue"

