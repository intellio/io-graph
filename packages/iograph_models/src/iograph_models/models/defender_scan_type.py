from __future__ import annotations
from enum import StrEnum


class DefenderScanType(StrEnum):
	userDefined = "userDefined"
	disabled = "disabled"
	quick = "quick"
	full = "full"

