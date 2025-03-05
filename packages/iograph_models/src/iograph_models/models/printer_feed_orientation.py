from __future__ import annotations
from enum import StrEnum


class PrinterFeedOrientation(StrEnum):
	longEdgeFirst = "longEdgeFirst"
	shortEdgeFirst = "shortEdgeFirst"
	unknownFutureValue = "unknownFutureValue"

