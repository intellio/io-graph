from __future__ import annotations
from enum import StrEnum


class MeteredConnectionLimitType(StrEnum):
	unrestricted = "unrestricted"
	fixed = "fixed"
	variable = "variable"

