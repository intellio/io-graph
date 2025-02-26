from __future__ import annotations
from enum import Enum


class ConditionalAccessPolicyState(Enum):
	enabled = "enabled"
	disabled = "disabled"
	enabledForReportingButNotEnforced = "enabledForReportingButNotEnforced"

