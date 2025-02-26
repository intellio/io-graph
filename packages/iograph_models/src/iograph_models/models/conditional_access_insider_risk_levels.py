from __future__ import annotations
from enum import Enum


class ConditionalAccessInsiderRiskLevels(Enum):
	minor = "minor"
	moderate = "moderate"
	elevated = "elevated"
	unknownFutureValue = "unknownFutureValue"

