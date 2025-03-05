from __future__ import annotations
from enum import StrEnum


class RestoreSessionStatus(StrEnum):
	draft = "draft"
	activating = "activating"
	active = "active"
	completedWithError = "completedWithError"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"
	failed = "failed"

