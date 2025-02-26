from __future__ import annotations
from enum import Enum


class SecuritySensorHealthStatus(Enum):
	healthy = "healthy"
	notHealthyLow = "notHealthyLow"
	notHealthyMedium = "notHealthyMedium"
	notHealthyHigh = "notHealthyHigh"
	unknownFutureValue = "unknownFutureValue"

