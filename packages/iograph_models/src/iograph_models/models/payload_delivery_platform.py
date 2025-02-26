from __future__ import annotations
from enum import Enum


class PayloadDeliveryPlatform(Enum):
	unknown = "unknown"
	sms = "sms"
	email = "email"
	teams = "teams"
	unknownFutureValue = "unknownFutureValue"

