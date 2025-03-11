from __future__ import annotations
from enum import StrEnum


class UserExperienceAnalyticsDeviceStatus(StrEnum):
	anomalous = "anomalous"
	affected = "affected"
	atRisk = "atRisk"
	unknownFutureValue = "unknownFutureValue"

