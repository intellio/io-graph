from __future__ import annotations
from enum import Enum


class SecurityHostReputationRuleSeverity(Enum):
	unknown = "unknown"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

