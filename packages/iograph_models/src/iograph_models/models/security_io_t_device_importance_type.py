from __future__ import annotations
from enum import Enum


class SecurityIoTDeviceImportanceType(Enum):
	unknown = "unknown"
	low = "low"
	normal = "normal"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

