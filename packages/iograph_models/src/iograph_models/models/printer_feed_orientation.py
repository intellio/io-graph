from __future__ import annotations
from enum import Enum


class PrinterFeedOrientation(Enum):
	longEdgeFirst = "longEdgeFirst"
	shortEdgeFirst = "shortEdgeFirst"
	unknownFutureValue = "unknownFutureValue"

