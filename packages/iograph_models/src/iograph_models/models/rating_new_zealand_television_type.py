from __future__ import annotations
from enum import Enum


class RatingNewZealandTelevisionType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	adults = "adults"

