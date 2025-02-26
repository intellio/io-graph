from __future__ import annotations
from enum import Enum


class SecurityHostPortStatus(Enum):
	open = "open"
	filtered = "filtered"
	closed = "closed"
	unknownFutureValue = "unknownFutureValue"

