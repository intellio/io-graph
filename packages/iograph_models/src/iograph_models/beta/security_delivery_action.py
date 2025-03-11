from __future__ import annotations
from enum import StrEnum


class SecurityDeliveryAction(StrEnum):
	unknown = "unknown"
	deliveredToJunk = "deliveredToJunk"
	delivered = "delivered"
	blocked = "blocked"
	replaced = "replaced"
	unknownFutureValue = "unknownFutureValue"

