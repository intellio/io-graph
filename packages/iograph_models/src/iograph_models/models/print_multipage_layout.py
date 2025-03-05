from __future__ import annotations
from enum import StrEnum


class PrintMultipageLayout(StrEnum):
	clockwiseFromTopLeft = "clockwiseFromTopLeft"
	counterclockwiseFromTopLeft = "counterclockwiseFromTopLeft"
	counterclockwiseFromTopRight = "counterclockwiseFromTopRight"
	clockwiseFromTopRight = "clockwiseFromTopRight"
	counterclockwiseFromBottomLeft = "counterclockwiseFromBottomLeft"
	clockwiseFromBottomLeft = "clockwiseFromBottomLeft"
	counterclockwiseFromBottomRight = "counterclockwiseFromBottomRight"
	clockwiseFromBottomRight = "clockwiseFromBottomRight"
	unknownFutureValue = "unknownFutureValue"

