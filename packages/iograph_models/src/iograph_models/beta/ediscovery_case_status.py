from __future__ import annotations
from enum import StrEnum


class EdiscoveryCaseStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	pendingDelete = "pendingDelete"
	closing = "closing"
	closed = "closed"
	closedWithError = "closedWithError"

