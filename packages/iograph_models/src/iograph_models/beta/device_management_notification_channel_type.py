from __future__ import annotations
from enum import StrEnum


class DeviceManagementNotificationChannelType(StrEnum):
	portal = "portal"
	email = "email"
	phoneCall = "phoneCall"
	sms = "sms"
	unknownFutureValue = "unknownFutureValue"

