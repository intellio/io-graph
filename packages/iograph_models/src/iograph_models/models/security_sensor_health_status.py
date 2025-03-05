from __future__ import annotations
from enum import StrEnum


class SecuritySensorHealthStatus(StrEnum):
	healthy = "healthy"
	notHealthyLow = "notHealthyLow"
	notHealthyMedium = "notHealthyMedium"
	notHealthyHigh = "notHealthyHigh"
	unknownFutureValue = "unknownFutureValue"

