from __future__ import annotations
from enum import StrEnum


class RatingGermanyTelevisionType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	agesAbove6 = "agesAbove6"
	agesAbove12 = "agesAbove12"
	agesAbove16 = "agesAbove16"
	adults = "adults"

