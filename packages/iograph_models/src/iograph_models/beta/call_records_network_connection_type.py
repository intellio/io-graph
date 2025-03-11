from __future__ import annotations
from enum import StrEnum


class CallRecordsNetworkConnectionType(StrEnum):
	unknown = "unknown"
	wired = "wired"
	wifi = "wifi"
	mobile = "mobile"
	tunnel = "tunnel"
	unknownFutureValue = "unknownFutureValue"

