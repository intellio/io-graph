from __future__ import annotations
from enum import StrEnum


class ConditionalAccessInsiderRiskLevels(StrEnum):
	minor = "minor"
	moderate = "moderate"
	elevated = "elevated"
	unknownFutureValue = "unknownFutureValue"

