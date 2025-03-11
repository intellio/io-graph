from __future__ import annotations
from enum import StrEnum


class TrainingStatus(StrEnum):
	unknown = "unknown"
	assigned = "assigned"
	inProgress = "inProgress"
	completed = "completed"
	overdue = "overdue"
	unknownFutureValue = "unknownFutureValue"

