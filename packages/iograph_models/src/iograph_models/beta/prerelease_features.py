from __future__ import annotations
from enum import StrEnum


class PrereleaseFeatures(StrEnum):
	userDefined = "userDefined"
	settingsOnly = "settingsOnly"
	settingsAndExperimentations = "settingsAndExperimentations"
	notAllowed = "notAllowed"

