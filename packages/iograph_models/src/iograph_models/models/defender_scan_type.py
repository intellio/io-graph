from __future__ import annotations
from enum import Enum


class DefenderScanType(Enum):
	userDefined = "userDefined"
	disabled = "disabled"
	quick = "quick"
	full = "full"

