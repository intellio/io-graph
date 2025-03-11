from __future__ import annotations
from enum import StrEnum


class TeamworkDeviceActivityState(StrEnum):
	unknown = "unknown"
	busy = "busy"
	idle = "idle"
	unavailable = "unavailable"
	unknownFutureValue = "unknownFutureValue"

