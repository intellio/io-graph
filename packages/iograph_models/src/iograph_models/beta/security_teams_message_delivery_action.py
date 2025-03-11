from __future__ import annotations
from enum import StrEnum


class SecurityTeamsMessageDeliveryAction(StrEnum):
	unknown = "unknown"
	deliveredAsSpam = "deliveredAsSpam"
	delivered = "delivered"
	blocked = "blocked"
	replaced = "replaced"
	unknownFutureValue = "unknownFutureValue"

