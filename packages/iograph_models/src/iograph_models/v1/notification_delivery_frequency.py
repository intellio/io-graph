from __future__ import annotations
from enum import StrEnum


class NotificationDeliveryFrequency(StrEnum):
	unknown = "unknown"
	weekly = "weekly"
	biWeekly = "biWeekly"
	unknownFutureValue = "unknownFutureValue"

