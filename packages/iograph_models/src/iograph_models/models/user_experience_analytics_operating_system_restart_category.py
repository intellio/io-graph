from __future__ import annotations
from enum import Enum


class UserExperienceAnalyticsOperatingSystemRestartCategory(Enum):
	unknown = "unknown"
	restartWithUpdate = "restartWithUpdate"
	restartWithoutUpdate = "restartWithoutUpdate"
	blueScreen = "blueScreen"
	shutdownWithUpdate = "shutdownWithUpdate"
	shutdownWithoutUpdate = "shutdownWithoutUpdate"
	longPowerButtonPress = "longPowerButtonPress"
	bootError = "bootError"
	update = "update"
	unknownFutureValue = "unknownFutureValue"

