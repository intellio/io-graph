from __future__ import annotations
from enum import StrEnum


class ComplianceState(StrEnum):
	unknown = "unknown"
	compliant = "compliant"
	noncompliant = "noncompliant"
	conflict = "conflict"
	error = "error"
	inGracePeriod = "inGracePeriod"
	configManager = "configManager"

