from __future__ import annotations
from enum import StrEnum


class TiAction(StrEnum):
	unknown = "unknown"
	allow = "allow"
	block = "block"
	alert = "alert"
	unknownFutureValue = "unknownFutureValue"

