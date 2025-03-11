from __future__ import annotations
from enum import StrEnum


class PolicyPlatformType(StrEnum):
	android = "android"
	androidForWork = "androidForWork"
	iOS = "iOS"
	macOS = "macOS"
	windowsPhone81 = "windowsPhone81"
	windows81AndLater = "windows81AndLater"
	windows10AndLater = "windows10AndLater"
	androidWorkProfile = "androidWorkProfile"
	windows10XProfile = "windows10XProfile"
	androidAOSP = "androidAOSP"
	all = "all"

