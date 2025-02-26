from __future__ import annotations
from enum import Enum


class CloudPcDeviceImageOsStatus(Enum):
	supported = "supported"
	supportedWithWarning = "supportedWithWarning"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

