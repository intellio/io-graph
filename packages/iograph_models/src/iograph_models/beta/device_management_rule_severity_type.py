from __future__ import annotations
from enum import StrEnum


class DeviceManagementRuleSeverityType(StrEnum):
	unknown = "unknown"
	informational = "informational"
	warning = "warning"
	critical = "critical"
	unknownFutureValue = "unknownFutureValue"

