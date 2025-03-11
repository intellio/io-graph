from __future__ import annotations
from enum import StrEnum


class EndUserNotificationPreference(StrEnum):
	unknown = "unknown"
	microsoft = "microsoft"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

