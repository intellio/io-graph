from __future__ import annotations
from enum import Enum


class ProtectionRuleStatus(Enum):
	draft = "draft"
	active = "active"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	unknownFutureValue = "unknownFutureValue"

