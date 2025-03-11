from __future__ import annotations
from enum import StrEnum


class WindowsSModeConfiguration(StrEnum):
	noRestriction = "noRestriction"
	block = "block"
	unlock = "unlock"

