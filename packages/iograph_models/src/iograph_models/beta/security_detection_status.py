from __future__ import annotations
from enum import StrEnum


class SecurityDetectionStatus(StrEnum):
	detected = "detected"
	blocked = "blocked"
	prevented = "prevented"
	unknownFutureValue = "unknownFutureValue"

