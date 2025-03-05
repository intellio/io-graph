from __future__ import annotations
from enum import StrEnum


class SecurityHostPortStatus(StrEnum):
	open = "open"
	filtered = "filtered"
	closed = "closed"
	unknownFutureValue = "unknownFutureValue"

