from __future__ import annotations
from enum import StrEnum


class MicrosoftTunnelLogCollectionStatus(StrEnum):
	pending = "pending"
	completed = "completed"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

