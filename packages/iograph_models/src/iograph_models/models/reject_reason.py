from __future__ import annotations
from enum import Enum


class RejectReason(Enum):
	none = "none"
	busy = "busy"
	forbidden = "forbidden"
	unknownFutureValue = "unknownFutureValue"

