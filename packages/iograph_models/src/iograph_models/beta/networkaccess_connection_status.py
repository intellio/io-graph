from __future__ import annotations
from enum import StrEnum


class NetworkaccessConnectionStatus(StrEnum):
	open = "open"
	active = "active"
	closed = "closed"
	unknownFutureValue = "unknownFutureValue"

