from __future__ import annotations
from enum import Enum


class CourseStatus(Enum):
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"

