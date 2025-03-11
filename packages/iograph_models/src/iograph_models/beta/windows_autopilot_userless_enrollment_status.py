from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotUserlessEnrollmentStatus(StrEnum):
	unknown = "unknown"
	allowed = "allowed"
	blocked = "blocked"
	unknownFutureValue = "unknownFutureValue"

