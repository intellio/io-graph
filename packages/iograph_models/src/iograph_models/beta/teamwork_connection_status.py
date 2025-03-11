from __future__ import annotations
from enum import StrEnum


class TeamworkConnectionStatus(StrEnum):
	unknown = "unknown"
	connected = "connected"
	disconnected = "disconnected"
	unknownFutureValue = "unknownFutureValue"

