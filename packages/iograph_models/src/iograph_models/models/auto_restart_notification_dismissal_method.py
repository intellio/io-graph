from __future__ import annotations
from enum import Enum


class AutoRestartNotificationDismissalMethod(Enum):
	notConfigured = "notConfigured"
	automatic = "automatic"
	user = "user"
	unknownFutureValue = "unknownFutureValue"

