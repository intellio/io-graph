from __future__ import annotations
from enum import Enum


class RatingUnitedKingdomMoviesType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	universalChildren = "universalChildren"
	parentalGuidance = "parentalGuidance"
	agesAbove12Video = "agesAbove12Video"
	agesAbove12Cinema = "agesAbove12Cinema"
	agesAbove15 = "agesAbove15"
	adults = "adults"

