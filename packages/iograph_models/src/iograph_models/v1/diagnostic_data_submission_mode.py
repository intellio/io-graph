from __future__ import annotations
from enum import StrEnum


class DiagnosticDataSubmissionMode(StrEnum):
	userDefined = "userDefined"
	none = "none"
	basic = "basic"
	enhanced = "enhanced"
	full = "full"

