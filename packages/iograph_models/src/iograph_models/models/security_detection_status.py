from __future__ import annotations
from enum import Enum


class SecurityDetectionStatus(Enum):
	detected = "detected"
	blocked = "blocked"
	prevented = "prevented"
	unknownFutureValue = "unknownFutureValue"

