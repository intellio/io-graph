from __future__ import annotations
from enum import StrEnum


class TeamworkCallEventType(StrEnum):
	call = "call"
	meeting = "meeting"
	screenShare = "screenShare"
	unknownFutureValue = "unknownFutureValue"

