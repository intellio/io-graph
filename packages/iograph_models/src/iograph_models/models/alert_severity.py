from __future__ import annotations
from enum import Enum


class AlertSeverity(Enum):
	unknown = "unknown"
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

