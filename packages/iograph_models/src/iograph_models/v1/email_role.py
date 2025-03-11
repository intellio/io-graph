from __future__ import annotations
from enum import StrEnum


class EmailRole(StrEnum):
	unknown = "unknown"
	sender = "sender"
	recipient = "recipient"
	unknownFutureValue = "unknownFutureValue"

