from __future__ import annotations
from enum import Enum


class SecurityDeviceRiskScore(Enum):
	none = "none"
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

