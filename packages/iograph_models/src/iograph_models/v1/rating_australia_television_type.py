from __future__ import annotations
from enum import StrEnum


class RatingAustraliaTelevisionType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	preschoolers = "preschoolers"
	children = "children"
	general = "general"
	parentalGuidance = "parentalGuidance"
	mature = "mature"
	agesAbove15 = "agesAbove15"
	agesAbove15AdultViolence = "agesAbove15AdultViolence"

