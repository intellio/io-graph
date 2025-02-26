from __future__ import annotations
from enum import Enum


class ProcessIntegrityLevel(Enum):
	unknown = "unknown"
	untrusted = "untrusted"
	low = "low"
	medium = "medium"
	high = "high"
	system = "system"
	unknownFutureValue = "unknownFutureValue"

