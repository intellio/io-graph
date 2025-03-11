from __future__ import annotations
from enum import StrEnum


class NetworkaccessConnectivityState(StrEnum):
	pending = "pending"
	connected = "connected"
	inactive = "inactive"
	error = "error"
	unknownFutureValue = "unknownFutureValue"

