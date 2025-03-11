from __future__ import annotations
from enum import StrEnum


class RejectReason(StrEnum):
	none = "none"
	busy = "busy"
	forbidden = "forbidden"
	unknownFutureValue = "unknownFutureValue"

