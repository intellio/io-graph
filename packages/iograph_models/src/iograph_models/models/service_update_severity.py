from __future__ import annotations
from enum import StrEnum


class ServiceUpdateSeverity(StrEnum):
	normal = "normal"
	high = "high"
	critical = "critical"
	unknownFutureValue = "unknownFutureValue"

