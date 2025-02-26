from __future__ import annotations
from enum import Enum


class TaskStatus(Enum):
	notStarted = "notStarted"
	inProgress = "inProgress"
	completed = "completed"
	waitingOnOthers = "waitingOnOthers"
	deferred = "deferred"

