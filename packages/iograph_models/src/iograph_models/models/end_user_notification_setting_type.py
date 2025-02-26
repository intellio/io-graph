from __future__ import annotations
from enum import Enum


class EndUserNotificationSettingType(Enum):
	unknown = "unknown"
	noTraining = "noTraining"
	trainingSelected = "trainingSelected"
	noNotification = "noNotification"
	unknownFutureValue = "unknownFutureValue"

