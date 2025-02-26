from __future__ import annotations
from enum import Enum


class RatingCanadaMoviesType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	agesAbove14 = "agesAbove14"
	agesAbove18 = "agesAbove18"
	restricted = "restricted"

