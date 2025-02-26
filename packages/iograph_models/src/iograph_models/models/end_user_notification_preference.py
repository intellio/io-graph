from __future__ import annotations
from enum import Enum


class EndUserNotificationPreference(Enum):
	unknown = "unknown"
	microsoft = "microsoft"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

