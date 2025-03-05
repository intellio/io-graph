from __future__ import annotations
from enum import StrEnum


class PayloadDeliveryPlatform(StrEnum):
	unknown = "unknown"
	sms = "sms"
	email = "email"
	teams = "teams"
	unknownFutureValue = "unknownFutureValue"

