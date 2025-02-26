from __future__ import annotations
from enum import Enum


class PrintMultipageLayout(Enum):
	clockwiseFromTopLeft = "clockwiseFromTopLeft"
	counterclockwiseFromTopLeft = "counterclockwiseFromTopLeft"
	counterclockwiseFromTopRight = "counterclockwiseFromTopRight"
	clockwiseFromTopRight = "clockwiseFromTopRight"
	counterclockwiseFromBottomLeft = "counterclockwiseFromBottomLeft"
	clockwiseFromBottomLeft = "clockwiseFromBottomLeft"
	counterclockwiseFromBottomRight = "counterclockwiseFromBottomRight"
	clockwiseFromBottomRight = "clockwiseFromBottomRight"
	unknownFutureValue = "unknownFutureValue"

