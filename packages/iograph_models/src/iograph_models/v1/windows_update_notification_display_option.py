from __future__ import annotations
from enum import StrEnum


class WindowsUpdateNotificationDisplayOption(StrEnum):
	notConfigured = "notConfigured"
	defaultNotifications = "defaultNotifications"
	restartWarningsOnly = "restartWarningsOnly"
	disableAllNotifications = "disableAllNotifications"
	unknownFutureValue = "unknownFutureValue"

