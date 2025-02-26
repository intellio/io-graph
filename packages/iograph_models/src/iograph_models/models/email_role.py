from __future__ import annotations
from enum import Enum


class EmailRole(Enum):
	unknown = "unknown"
	sender = "sender"
	recipient = "recipient"
	unknownFutureValue = "unknownFutureValue"

