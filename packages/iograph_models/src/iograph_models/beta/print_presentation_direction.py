from __future__ import annotations
from enum import StrEnum


class PrintPresentationDirection(StrEnum):
	clockwiseFromTopLeft = "clockwiseFromTopLeft"
	counterClockwiseFromTopLeft = "counterClockwiseFromTopLeft"
	counterClockwiseFromTopRight = "counterClockwiseFromTopRight"
	clockwiseFromTopRight = "clockwiseFromTopRight"
	counterClockwiseFromBottomLeft = "counterClockwiseFromBottomLeft"
	clockwiseFromBottomLeft = "clockwiseFromBottomLeft"
	counterClockwiseFromBottomRight = "counterClockwiseFromBottomRight"
	clockwiseFromBottomRight = "clockwiseFromBottomRight"

