from __future__ import annotations
from enum import StrEnum


class ManagedTenantsAlertSeverity(StrEnum):
	unknown = "unknown"
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

