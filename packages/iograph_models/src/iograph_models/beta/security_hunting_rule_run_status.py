from __future__ import annotations
from enum import StrEnum


class SecurityHuntingRuleRunStatus(StrEnum):
	running = "running"
	completed = "completed"
	failed = "failed"
	partiallyFailed = "partiallyFailed"
	unknownFutureValue = "unknownFutureValue"

