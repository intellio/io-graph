from __future__ import annotations
from enum import Enum


class SecurityCaseStatus(Enum):
	unknown = "unknown"
	active = "active"
	pendingDelete = "pendingDelete"
	closing = "closing"
	closed = "closed"
	closedWithError = "closedWithError"
	unknownFutureValue = "unknownFutureValue"

