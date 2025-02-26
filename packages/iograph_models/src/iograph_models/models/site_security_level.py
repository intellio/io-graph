from __future__ import annotations
from enum import Enum


class SiteSecurityLevel(Enum):
	userDefined = "userDefined"
	low = "low"
	mediumLow = "mediumLow"
	medium = "medium"
	mediumHigh = "mediumHigh"
	high = "high"

