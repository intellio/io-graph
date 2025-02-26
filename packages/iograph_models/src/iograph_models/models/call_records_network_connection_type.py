from __future__ import annotations
from enum import Enum


class CallRecordsNetworkConnectionType(Enum):
	unknown = "unknown"
	wired = "wired"
	wifi = "wifi"
	mobile = "mobile"
	tunnel = "tunnel"
	unknownFutureValue = "unknownFutureValue"

