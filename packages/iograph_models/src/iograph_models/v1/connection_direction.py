from __future__ import annotations
from enum import StrEnum


class ConnectionDirection(StrEnum):
	unknown = "unknown"
	inbound = "inbound"
	outbound = "outbound"
	unknownFutureValue = "unknownFutureValue"

