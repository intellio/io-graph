from __future__ import annotations
from enum import StrEnum


class SecurityCaseStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	pendingDelete = "pendingDelete"
	closing = "closing"
	closed = "closed"
	closedWithError = "closedWithError"
	unknownFutureValue = "unknownFutureValue"

