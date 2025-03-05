from __future__ import annotations
from enum import StrEnum


class RatingIrelandTelevisionType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	general = "general"
	children = "children"
	youngAdults = "youngAdults"
	parentalSupervision = "parentalSupervision"
	mature = "mature"

