from __future__ import annotations
from enum import Enum


class PolicyPlatformType(Enum):
	android = "android"
	androidForWork = "androidForWork"
	iOS = "iOS"
	macOS = "macOS"
	windowsPhone81 = "windowsPhone81"
	windows81AndLater = "windows81AndLater"
	windows10AndLater = "windows10AndLater"
	all = "all"

