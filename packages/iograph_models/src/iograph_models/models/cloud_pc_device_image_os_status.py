from __future__ import annotations
from enum import StrEnum


class CloudPcDeviceImageOsStatus(StrEnum):
	supported = "supported"
	supportedWithWarning = "supportedWithWarning"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

