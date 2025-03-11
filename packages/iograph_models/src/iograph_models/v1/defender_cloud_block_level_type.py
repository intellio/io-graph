from __future__ import annotations
from enum import StrEnum


class DefenderCloudBlockLevelType(StrEnum):
	notConfigured = "notConfigured"
	high = "high"
	highPlus = "highPlus"
	zeroTolerance = "zeroTolerance"

