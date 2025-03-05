from __future__ import annotations
from enum import StrEnum


class AlertSeverity(StrEnum):
	unknown = "unknown"
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

