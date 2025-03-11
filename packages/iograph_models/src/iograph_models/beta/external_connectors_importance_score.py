from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsImportanceScore(StrEnum):
	low = "low"
	medium = "medium"
	high = "high"
	veryHigh = "veryHigh"
	unknownFutureValue = "unknownFutureValue"

