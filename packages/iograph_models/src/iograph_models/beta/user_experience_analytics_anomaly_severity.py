from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsAnomalySeverity(StrEnum):
	high = "high"
	medium = "medium"
	low = "low"
	informational = "informational"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

