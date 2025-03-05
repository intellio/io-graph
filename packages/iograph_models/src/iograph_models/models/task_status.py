from __future__ import annotations
from enum import StrEnum


class TaskStatus(StrEnum):
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	waitingOnOthers = "waitingOnOthers"
	deferred = "deferred"

