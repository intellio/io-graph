from __future__ import annotations
from enum import Enum


class RatingUnitedStatesTelevisionType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	childrenAll = "childrenAll"
	childrenAbove7 = "childrenAbove7"
	general = "general"
	parentalGuidance = "parentalGuidance"
	childrenAbove14 = "childrenAbove14"
	adults = "adults"

