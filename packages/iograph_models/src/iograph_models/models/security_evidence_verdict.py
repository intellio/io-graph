from __future__ import annotations
from enum import Enum


class SecurityEvidenceVerdict(Enum):
	unknown = "unknown"
	suspicious = "suspicious"
	malicious = "malicious"
	noThreatsFound = "noThreatsFound"
	unknownFutureValue = "unknownFutureValue"

