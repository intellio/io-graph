from __future__ import annotations
from enum import StrEnum


class Platform(StrEnum):
	unknown = "unknown"
	ios = "ios"
	android = "android"
	windows = "windows"
	windowsMobile = "windowsMobile"
	macOS = "macOS"
	visionOS = "visionOS"
	tvOS = "tvOS"
	unknownFutureValue = "unknownFutureValue"

