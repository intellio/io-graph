from __future__ import annotations
from enum import StrEnum


class DefenderProtectionType(StrEnum):
	userDefined = "userDefined"
	enable = "enable"
	auditMode = "auditMode"
	warn = "warn"
	notConfigured = "notConfigured"

