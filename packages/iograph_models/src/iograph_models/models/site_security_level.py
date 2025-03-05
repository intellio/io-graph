from __future__ import annotations
from enum import StrEnum


class SiteSecurityLevel(StrEnum):
	userDefined = "userDefined"
	low = "low"
	mediumLow = "mediumLow"
	medium = "medium"
	mediumHigh = "mediumHigh"
	high = "high"

