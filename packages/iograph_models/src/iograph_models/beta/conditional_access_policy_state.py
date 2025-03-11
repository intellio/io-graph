from __future__ import annotations
from enum import StrEnum


class ConditionalAccessPolicyState(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	enabledForReportingButNotEnforced = "enabledForReportingButNotEnforced"

