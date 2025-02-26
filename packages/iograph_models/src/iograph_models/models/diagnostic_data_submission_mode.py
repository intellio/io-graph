from __future__ import annotations
from enum import Enum


class DiagnosticDataSubmissionMode(Enum):
	userDefined = "userDefined"
	none = "none"
	basic = "basic"
	enhanced = "enhanced"
	full = "full"

