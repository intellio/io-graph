from __future__ import annotations
from enum import StrEnum


class DetectedAppPlatformType(StrEnum):
	unknown = "unknown"
	windows = "windows"
	windowsMobile = "windowsMobile"
	windowsHolographic = "windowsHolographic"
	ios = "ios"
	macOS = "macOS"
	chromeOS = "chromeOS"
	androidOSP = "androidOSP"
	androidDeviceAdministrator = "androidDeviceAdministrator"
	androidWorkProfile = "androidWorkProfile"
	androidDedicatedAndFullyManaged = "androidDedicatedAndFullyManaged"
	unknownFutureValue = "unknownFutureValue"

