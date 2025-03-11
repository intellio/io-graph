from __future__ import annotations
from enum import StrEnum


class InsiderRiskLevel(StrEnum):
	none = "none"
	minor = "minor"
	moderate = "moderate"
	elevated = "elevated"
	unknownFutureValue = "unknownFutureValue"

