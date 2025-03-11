from __future__ import annotations
from enum import StrEnum


class SecurityHostReputationClassification(StrEnum):
	unknown = "unknown"
	neutral = "neutral"
	suspicious = "suspicious"
	malicious = "malicious"
	unknownFutureValue = "unknownFutureValue"

