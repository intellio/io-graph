from __future__ import annotations
from enum import Enum


class SecurityHealthIssueSeverity(Enum):
	low = "low"
	medium = "medium"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

