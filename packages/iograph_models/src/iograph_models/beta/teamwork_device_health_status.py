from __future__ import annotations
from enum import StrEnum


class TeamworkDeviceHealthStatus(StrEnum):
	unknown = "unknown"
	offline = "offline"
	critical = "critical"
	nonUrgent = "nonUrgent"
	healthy = "healthy"
	unknownFutureValue = "unknownFutureValue"

