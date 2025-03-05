from __future__ import annotations
from enum import StrEnum


class RiskDetectionTimingType(StrEnum):
	notDefined = "notDefined"
	realtime = "realtime"
	nearRealtime = "nearRealtime"
	offline = "offline"
	unknownFutureValue = "unknownFutureValue"

