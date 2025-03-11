from __future__ import annotations
from enum import StrEnum


class SecurityHostReputationRuleSeverity(StrEnum):
	unknown = "unknown"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

