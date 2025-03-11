from __future__ import annotations
from enum import StrEnum


class WorkplaceSensorEventType(StrEnum):
	badgeIn = "badgeIn"
	badgeOut = "badgeOut"
	unknownFutureValue = "unknownFutureValue"

