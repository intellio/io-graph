from __future__ import annotations
from enum import StrEnum


class SecurityDeviceRiskScore(StrEnum):
	none = "none"
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

