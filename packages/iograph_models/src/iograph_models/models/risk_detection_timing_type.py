from __future__ import annotations
from enum import Enum


class RiskDetectionTimingType(Enum):
	notDefined = "notDefined"
	realtime = "realtime"
	nearRealtime = "nearRealtime"
	offline = "offline"
	unknownFutureValue = "unknownFutureValue"

