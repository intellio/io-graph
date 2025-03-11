from __future__ import annotations
from enum import StrEnum


class NetworkaccessAlertSeverity(StrEnum):
	informational = "informational"
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

