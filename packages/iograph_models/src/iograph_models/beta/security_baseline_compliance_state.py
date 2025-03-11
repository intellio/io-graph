from __future__ import annotations
from enum import StrEnum


class SecurityBaselineComplianceState(StrEnum):
	unknown = "unknown"
	secure = "secure"
	notApplicable = "notApplicable"
	notSecure = "notSecure"
	error = "error"
	conflict = "conflict"

