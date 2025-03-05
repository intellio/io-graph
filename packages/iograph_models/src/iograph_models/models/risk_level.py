from __future__ import annotations
from enum import StrEnum


class RiskLevel(StrEnum):
	low = "low"
	medium = "medium"
	high = "high"
	hidden = "hidden"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

