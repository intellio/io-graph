from __future__ import annotations
from enum import Enum


class ThreatAssessmentResultType(Enum):
	checkPolicy = "checkPolicy"
	rescan = "rescan"
	unknownFutureValue = "unknownFutureValue"

