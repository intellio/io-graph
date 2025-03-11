from __future__ import annotations
from enum import StrEnum


class RatingFranceMoviesType(StrEnum):
	allAllowed = "allAllowed"
	allBlocked = "allBlocked"
	agesAbove10 = "agesAbove10"
	agesAbove12 = "agesAbove12"
	agesAbove16 = "agesAbove16"
	agesAbove18 = "agesAbove18"

