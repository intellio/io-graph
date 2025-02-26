from __future__ import annotations
from enum import Enum


class NotificationDeliveryPreference(Enum):
	unknown = "unknown"
	deliverImmedietly = "deliverImmedietly"
	deliverAfterCampaignEnd = "deliverAfterCampaignEnd"
	unknownFutureValue = "unknownFutureValue"

