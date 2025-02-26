from __future__ import annotations
from enum import Enum


class TrainingStatus(Enum):
	unknown = "unknown"
	assigned = "assigned"
	inProgress = "inProgress"
	completed = "completed"
	overdue = "overdue"
	unknownFutureValue = "unknownFutureValue"

