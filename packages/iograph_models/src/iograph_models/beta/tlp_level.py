from __future__ import annotations
from enum import StrEnum


class TlpLevel(StrEnum):
	unknown = "unknown"
	white = "white"
	green = "green"
	amber = "amber"
	red = "red"
	unknownFutureValue = "unknownFutureValue"

