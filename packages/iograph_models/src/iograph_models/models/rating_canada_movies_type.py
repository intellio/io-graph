from __future__ import annotations
from enum import StrEnum


class RatingCanadaMoviesType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	agesAbove14 = "agesAbove14"
	agesAbove18 = "agesAbove18"
	restricted = "restricted"

