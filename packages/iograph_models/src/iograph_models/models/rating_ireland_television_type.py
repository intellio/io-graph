from __future__ import annotations
from enum import Enum


class RatingIrelandTelevisionType(Enum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	children = "children"
	youngAdults = "youngAdults"
	parentalSupervision = "parentalSupervision"
	mature = "mature"

