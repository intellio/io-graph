from __future__ import annotations
from enum import StrEnum


class RatingCanadaTelevisionType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	children = "children"
	childrenAbove8 = "childrenAbove8"
	general = "general"
	parentalGuidance = "parentalGuidance"
	agesAbove14 = "agesAbove14"
	agesAbove18 = "agesAbove18"

