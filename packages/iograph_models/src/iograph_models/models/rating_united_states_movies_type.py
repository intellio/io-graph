from __future__ import annotations
from enum import Enum


class RatingUnitedStatesMoviesType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	parentalGuidance13 = "parentalGuidance13"
	restricted = "restricted"
	adults = "adults"

