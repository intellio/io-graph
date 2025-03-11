from __future__ import annotations
from enum import StrEnum


class EnrollmentState(StrEnum):
	unknown = "unknown"
	enrolled = "enrolled"
	pendingReset = "pendingReset"
	failed = "failed"
	notContacted = "notContacted"
	blocked = "blocked"

