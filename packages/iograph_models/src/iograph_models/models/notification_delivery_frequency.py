from __future__ import annotations
from enum import Enum


class NotificationDeliveryFrequency(Enum):
	unknown = "unknown"
	weekly = "weekly"
	biWeekly = "biWeekly"
	unknownFutureValue = "unknownFutureValue"

