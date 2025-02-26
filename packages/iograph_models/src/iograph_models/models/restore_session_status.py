from __future__ import annotations
from enum import Enum


class RestoreSessionStatus(Enum):
	draft = "draft"
	activating = "activating"
	active = "active"
	completedWithError = "completedWithError"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"
	failed = "failed"

