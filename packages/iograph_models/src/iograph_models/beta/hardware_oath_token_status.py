from __future__ import annotations
from enum import StrEnum


class HardwareOathTokenStatus(StrEnum):
	available = "available"
	assigned = "assigned"
	activated = "activated"
	failedActivation = "failedActivation"
	unknownFutureValue = "unknownFutureValue"

