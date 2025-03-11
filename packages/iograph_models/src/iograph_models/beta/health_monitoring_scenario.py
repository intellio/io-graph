from __future__ import annotations
from enum import StrEnum


class HealthMonitoringScenario(StrEnum):
	unknown = "unknown"
	mfa = "mfa"
	devices = "devices"
	unknownFutureValue = "unknownFutureValue"

