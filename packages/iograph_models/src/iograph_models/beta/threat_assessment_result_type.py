from __future__ import annotations
from enum import StrEnum


class ThreatAssessmentResultType(StrEnum):
	checkPolicy = "checkPolicy"
	rescan = "rescan"
	unknownFutureValue = "unknownFutureValue"

