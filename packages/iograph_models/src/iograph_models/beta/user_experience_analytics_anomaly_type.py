from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsAnomalyType(StrEnum):
	device = "device"
	application = "application"
	stopError = "stopError"
	driver = "driver"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

