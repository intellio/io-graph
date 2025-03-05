from __future__ import annotations
from enum import StrEnum


class ConditionalAccessDevicePlatform(StrEnum):
	android = "android"
	iOS = "iOS"
	windows = "windows"
	windowsPhone = "windowsPhone"
	macOS = "macOS"
	all = "all"
	unknownFutureValue = "unknownFutureValue"
	linux = "linux"

