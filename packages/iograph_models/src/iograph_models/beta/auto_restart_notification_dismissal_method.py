from __future__ import annotations
from enum import StrEnum


class AutoRestartNotificationDismissalMethod(StrEnum):
	notConfigured = "notConfigured"
	automatic = "automatic"
	user = "user"
	unknownFutureValue = "unknownFutureValue"

