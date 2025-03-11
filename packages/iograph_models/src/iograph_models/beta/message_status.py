from __future__ import annotations
from enum import StrEnum


class MessageStatus(StrEnum):
	gettingStatus = "gettingStatus"
	pending = "pending"
	failed = "failed"
	delivered = "delivered"
	expanded = "expanded"
	quarantined = "quarantined"
	filteredAsSpam = "filteredAsSpam"
	unknownFutureValue = "unknownFutureValue"

