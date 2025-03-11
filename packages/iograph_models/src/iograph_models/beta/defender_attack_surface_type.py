from __future__ import annotations
from enum import StrEnum


class DefenderAttackSurfaceType(StrEnum):
	userDefined = "userDefined"
	block = "block"
	auditMode = "auditMode"
	warn = "warn"
	disable = "disable"

