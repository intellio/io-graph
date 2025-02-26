from __future__ import annotations
from enum import Enum


class TeamworkCallEventType(Enum):
	call = "call"
	meeting = "meeting"
	screenShare = "screenShare"
	unknownFutureValue = "unknownFutureValue"

