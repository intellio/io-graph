from __future__ import annotations
from enum import StrEnum


class WindowsDeviceType(StrEnum):
	none = "none"
	desktop = "desktop"
	mobile = "mobile"
	holographic = "holographic"
	team = "team"
	unknownFutureValue = "unknownFutureValue"

