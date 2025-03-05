from __future__ import annotations
from enum import StrEnum


class SecurityIoTDeviceImportanceType(StrEnum):
	unknown = "unknown"
	low = "low"
	normal = "normal"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

