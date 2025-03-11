from __future__ import annotations
from enum import StrEnum


class RatingAustraliaMoviesType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	mature = "mature"
	agesAbove15 = "agesAbove15"
	agesAbove18 = "agesAbove18"

