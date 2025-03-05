from __future__ import annotations
from enum import StrEnum


class RatingUnitedStatesMoviesType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	parentalGuidance13 = "parentalGuidance13"
	restricted = "restricted"
	adults = "adults"

