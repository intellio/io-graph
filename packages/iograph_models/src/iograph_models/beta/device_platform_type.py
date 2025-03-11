from __future__ import annotations
from enum import StrEnum


class DevicePlatformType(StrEnum):
	android = "android"
	androidForWork = "androidForWork"
	iOS = "iOS"
	macOS = "macOS"
	windowsPhone81 = "windowsPhone81"
	windows81AndLater = "windows81AndLater"
	windows10AndLater = "windows10AndLater"
	androidWorkProfile = "androidWorkProfile"
	unknown = "unknown"
	androidAOSP = "androidAOSP"
	androidMobileApplicationManagement = "androidMobileApplicationManagement"
	iOSMobileApplicationManagement = "iOSMobileApplicationManagement"
	unknownFutureValue = "unknownFutureValue"
	windowsMobileApplicationManagement = "windowsMobileApplicationManagement"

