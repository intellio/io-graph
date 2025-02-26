from __future__ import annotations
from enum import Enum


class SecurityHostReputationClassification(Enum):
	unknown = "unknown"
	neutral = "neutral"
	suspicious = "suspicious"
	malicious = "malicious"
	unknownFutureValue = "unknownFutureValue"

