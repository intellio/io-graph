from __future__ import annotations
from enum import StrEnum


class OperatingSystemUpgradeEligibility(StrEnum):
	upgraded = "upgraded"
	unknown = "unknown"
	notCapable = "notCapable"
	capable = "capable"
	unknownFutureValue = "unknownFutureValue"

