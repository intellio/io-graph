from __future__ import annotations
from enum import Enum


class SafeSearchFilterType(Enum):
	userDefined = "userDefined"
	strict = "strict"
	moderate = "moderate"

