from __future__ import annotations
from enum import Enum


class ServiceUpdateSeverity(Enum):
	normal = "normal"
	high = "high"
	critical = "critical"
	unknownFutureValue = "unknownFutureValue"

