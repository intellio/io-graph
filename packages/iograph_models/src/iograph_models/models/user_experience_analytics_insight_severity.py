from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsInsightSeverity(StrEnum):
	none = "none"
	informational = "informational"
	warning = "warning"
	error = "error"
	unknownFutureValue = "unknownFutureValue"

