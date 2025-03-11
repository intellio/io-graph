from __future__ import annotations
from enum import StrEnum


class SecurityEvidenceVerdict(StrEnum):
	unknown = "unknown"
	suspicious = "suspicious"
	malicious = "malicious"
	noThreatsFound = "noThreatsFound"
	unknownFutureValue = "unknownFutureValue"

