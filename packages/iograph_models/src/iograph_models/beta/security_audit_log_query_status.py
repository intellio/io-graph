from __future__ import annotations
from enum import StrEnum


class SecurityAuditLogQueryStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	cancelled = "cancelled"
	unknownFutureValue = "unknownFutureValue"

