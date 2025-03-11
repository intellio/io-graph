from __future__ import annotations
from enum import StrEnum


class CloudPcConnectivityStatus(StrEnum):
	unknown = "unknown"
	available = "available"
	availableWithWarning = "availableWithWarning"
	unavailable = "unavailable"
	unknownFutureValue = "unknownFutureValue"

