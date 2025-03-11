from __future__ import annotations
from enum import StrEnum


class CloudPcConnectivityEventResult(StrEnum):
	unknown = "unknown"
	success = "success"
	failure = "failure"
	unknownFutureValue = "unknownFutureValue"

