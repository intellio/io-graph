from __future__ import annotations
from enum import Enum


class PrereleaseFeatures(Enum):
	userDefined = "userDefined"
	settingsOnly = "settingsOnly"
	settingsAndExperimentations = "settingsAndExperimentations"
	notAllowed = "notAllowed"

