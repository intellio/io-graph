from __future__ import annotations
from enum import StrEnum


class SafeSearchFilterType(StrEnum):
	userDefined = "userDefined"
	strict = "strict"
	moderate = "moderate"

