from __future__ import annotations
from enum import Enum


class WindowsDeviceType(Enum):
	none = "none"
	desktop = "desktop"
	mobile = "mobile"
	holographic = "holographic"
	team = "team"
	unknownFutureValue = "unknownFutureValue"

