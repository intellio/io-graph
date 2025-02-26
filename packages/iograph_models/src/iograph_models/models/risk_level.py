from __future__ import annotations
from enum import Enum


class RiskLevel(Enum):
	low = "low"
	medium = "medium"
	high = "high"
	hidden = "hidden"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

