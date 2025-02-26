from __future__ import annotations
from enum import Enum


class SecurityDefaultRecordBehavior(Enum):
	startLocked = "startLocked"
	startUnlocked = "startUnlocked"
	unknownFutureValue = "unknownFutureValue"

