from __future__ import annotations
from enum import StrEnum


class DeviceCleanupRulePlatformType(StrEnum):
	all = "all"
	androidAOSP = "androidAOSP"
	androidDeviceAdministrator = "androidDeviceAdministrator"
	androidDedicatedAndFullyManagedCorporateOwnedWorkProfile = "androidDedicatedAndFullyManagedCorporateOwnedWorkProfile"
	chromeOS = "chromeOS"
	androidPersonallyOwnedWorkProfile = "androidPersonallyOwnedWorkProfile"
	ios = "ios"
	macOS = "macOS"
	windows = "windows"
	windowsHolographic = "windowsHolographic"
	unknownFutureValue = "unknownFutureValue"

