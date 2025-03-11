from __future__ import annotations
from enum import StrEnum


class WindowsDeviceUsageType(StrEnum):
	singleUser = "singleUser"
	shared = "shared"
	unknownFutureValue = "unknownFutureValue"

