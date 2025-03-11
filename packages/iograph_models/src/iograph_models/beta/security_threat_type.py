from __future__ import annotations
from enum import StrEnum


class SecurityThreatType(StrEnum):
	unknown = "unknown"
	spam = "spam"
	malware = "malware"
	phish = "phish"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

