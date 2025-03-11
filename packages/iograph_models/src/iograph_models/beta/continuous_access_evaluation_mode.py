from __future__ import annotations
from enum import StrEnum


class ContinuousAccessEvaluationMode(StrEnum):
	strictEnforcement = "strictEnforcement"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"
	strictLocation = "strictLocation"

