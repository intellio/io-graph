from __future__ import annotations
from enum import Enum


class OperatingSystemUpgradeEligibility(Enum):
	upgraded = "upgraded"
	unknown = "unknown"
	notCapable = "notCapable"
	capable = "capable"
	unknownFutureValue = "unknownFutureValue"

