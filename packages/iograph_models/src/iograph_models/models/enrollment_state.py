from __future__ import annotations
from enum import Enum


class EnrollmentState(Enum):
	unknown = "unknown"
	enrolled = "enrolled"
	pendingReset = "pendingReset"
	failed = "failed"
	notContacted = "notContacted"

