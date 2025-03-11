from __future__ import annotations
from enum import StrEnum


class SecurityTeamsDeliveryLocation(StrEnum):
	unknown = "unknown"
	teams = "teams"
	quarantine = "quarantine"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

