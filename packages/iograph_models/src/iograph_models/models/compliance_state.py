from __future__ import annotations
from enum import Enum


class ComplianceState(Enum):
	unknown = "unknown"
	compliant = "compliant"
	noncompliant = "noncompliant"
	conflict = "conflict"
	error = "error"
	inGracePeriod = "inGracePeriod"
	configManager = "configManager"

