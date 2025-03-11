from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoFedRampLevel(StrEnum):
	high = "high"
	moderate = "moderate"
	low = "low"
	liSaaS = "liSaaS"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"
	notSupported = "notSupported"

