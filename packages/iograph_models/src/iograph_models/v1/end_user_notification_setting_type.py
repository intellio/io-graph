from __future__ import annotations
from enum import StrEnum


class EndUserNotificationSettingType(StrEnum):
	unknown = "unknown"
	noTraining = "noTraining"
	trainingSelected = "trainingSelected"
	noNotification = "noNotification"
	unknownFutureValue = "unknownFutureValue"

