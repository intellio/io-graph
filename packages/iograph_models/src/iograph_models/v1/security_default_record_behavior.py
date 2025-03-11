from __future__ import annotations
from enum import StrEnum


class SecurityDefaultRecordBehavior(StrEnum):
	startLocked = "startLocked"
	startUnlocked = "startUnlocked"
	unknownFutureValue = "unknownFutureValue"

