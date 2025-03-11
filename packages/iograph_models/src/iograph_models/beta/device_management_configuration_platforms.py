from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationPlatforms(StrEnum):
	none = "none"
	android = "android"
	iOS = "iOS"
	macOS = "macOS"
	windows10X = "windows10X"
	windows10 = "windows10"
	linux = "linux"
	unknownFutureValue = "unknownFutureValue"
	androidEnterprise = "androidEnterprise"
	aosp = "aosp"

