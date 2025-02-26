from __future__ import annotations
from enum import Enum


class PrintDuplexMode(Enum):
	flipOnLongEdge = "flipOnLongEdge"
	flipOnShortEdge = "flipOnShortEdge"
	oneSided = "oneSided"
	unknownFutureValue = "unknownFutureValue"

