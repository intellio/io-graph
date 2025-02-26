from __future__ import annotations
from enum import Enum


class ConnectionDirection(Enum):
	unknown = "unknown"
	inbound = "inbound"
	outbound = "outbound"
	unknownFutureValue = "unknownFutureValue"

