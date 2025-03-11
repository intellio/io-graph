from __future__ import annotations
from enum import StrEnum


class EnrollmentRestrictionPlatformType(StrEnum):
	allPlatforms = "allPlatforms"
	ios = "ios"
	windows = "windows"
	windowsPhone = "windowsPhone"
	android = "android"
	androidForWork = "androidForWork"
	mac = "mac"
	linux = "linux"
	unknownFutureValue = "unknownFutureValue"

