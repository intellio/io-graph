from __future__ import annotations
from enum import Enum


class UserExperienceAnalyticsInsightSeverity(Enum):
	none = "none"
	informational = "informational"
	warning = "warning"
	error = "error"
	unknownFutureValue = "unknownFutureValue"

