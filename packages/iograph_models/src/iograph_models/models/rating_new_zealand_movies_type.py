from __future__ import annotations
from enum import Enum


class RatingNewZealandMoviesType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	mature = "mature"
	agesAbove13 = "agesAbove13"
	agesAbove15 = "agesAbove15"
	agesAbove16 = "agesAbove16"
	agesAbove18 = "agesAbove18"
	restricted = "restricted"
	agesAbove16Restricted = "agesAbove16Restricted"

