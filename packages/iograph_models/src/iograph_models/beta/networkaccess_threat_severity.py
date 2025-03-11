from __future__ import annotations
from enum import StrEnum


class NetworkaccessThreatSeverity(StrEnum):
	low = "low"
	medium = "medium"
	high = "high"
	critical = "critical"
	unknownFutureValue = "unknownFutureValue"

