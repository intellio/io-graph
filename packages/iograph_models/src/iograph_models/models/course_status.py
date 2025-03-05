from __future__ import annotations
from enum import StrEnum


class CourseStatus(StrEnum):
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"

