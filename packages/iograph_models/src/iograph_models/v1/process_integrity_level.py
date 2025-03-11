from __future__ import annotations
from enum import StrEnum


class ProcessIntegrityLevel(StrEnum):
	unknown = "unknown"
	untrusted = "untrusted"
	low = "low"
	medium = "medium"
	high = "high"
	system = "system"
	unknownFutureValue = "unknownFutureValue"

