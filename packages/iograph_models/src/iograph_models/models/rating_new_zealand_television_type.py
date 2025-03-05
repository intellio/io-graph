from __future__ import annotations
from enum import StrEnum


class RatingNewZealandTelevisionType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	parentalGuidance = "parentalGuidance"
	adults = "adults"

