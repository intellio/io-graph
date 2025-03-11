from __future__ import annotations
from enum import StrEnum


class PrintDuplexMode(StrEnum):
	flipOnLongEdge = "flipOnLongEdge"
	flipOnShortEdge = "flipOnShortEdge"
	oneSided = "oneSided"
	unknownFutureValue = "unknownFutureValue"

