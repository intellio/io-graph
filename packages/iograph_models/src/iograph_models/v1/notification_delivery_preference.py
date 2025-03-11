from __future__ import annotations
from enum import StrEnum


class NotificationDeliveryPreference(StrEnum):
	unknown = "unknown"
	deliverImmedietly = "deliverImmedietly"
	deliverAfterCampaignEnd = "deliverAfterCampaignEnd"
	unknownFutureValue = "unknownFutureValue"

