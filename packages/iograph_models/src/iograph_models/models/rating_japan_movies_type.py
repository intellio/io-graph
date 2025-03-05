from __future__ import annotations
from enum import StrEnum


class RatingJapanMoviesType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	agesAbove15 = "agesAbove15"
	agesAbove18 = "agesAbove18"

