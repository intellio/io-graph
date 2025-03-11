from __future__ import annotations
from enum import StrEnum


class ProtectionRuleStatus(StrEnum):
	draft = "draft"
	active = "active"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	unknownFutureValue = "unknownFutureValue"
	updateRequested = "updateRequested"
	deleteRequested = "deleteRequested"

