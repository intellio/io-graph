from __future__ import annotations
from enum import Enum


class RatingAppsType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	agesAbove4 = "agesAbove4"
	agesAbove9 = "agesAbove9"
	agesAbove12 = "agesAbove12"
	agesAbove17 = "agesAbove17"

