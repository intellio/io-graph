from __future__ import annotations
from enum import StrEnum


class ManagedTenantsNotificationDestination(StrEnum):
	none = "none"
	api = "api"
	email = "email"
	sms = "sms"
	unknownFutureValue = "unknownFutureValue"

