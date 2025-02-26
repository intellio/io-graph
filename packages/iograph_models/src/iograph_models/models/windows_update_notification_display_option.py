from __future__ import annotations
from enum import Enum


class WindowsUpdateNotificationDisplayOption(Enum):
	notConfigured = "notConfigured"
	defaultNotifications = "defaultNotifications"
	restartWarningsOnly = "restartWarningsOnly"
	disableAllNotifications = "disableAllNotifications"
	unknownFutureValue = "unknownFutureValue"

