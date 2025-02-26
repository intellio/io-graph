from __future__ import annotations
from enum import Enum


class ConditionalAccessDevicePlatform(Enum):
	android = "android"
	iOS = "iOS"
	windows = "windows"
	windowsPhone = "windowsPhone"
	macOS = "macOS"
	all = "all"
	unknownFutureValue = "unknownFutureValue"
	linux = "linux"

