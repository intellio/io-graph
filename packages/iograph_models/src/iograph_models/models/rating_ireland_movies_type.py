from __future__ import annotations
from enum import Enum


class RatingIrelandMoviesType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	agesAbove12 = "agesAbove12"
	agesAbove15 = "agesAbove15"
	agesAbove16 = "agesAbove16"
	adults = "adults"

