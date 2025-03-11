from __future__ import annotations
from enum import StrEnum


class PrintColorMode(StrEnum):
	blackAndWhite = "blackAndWhite"
	grayscale = "grayscale"
	color = "color"
	auto = "auto"
	unknownFutureValue = "unknownFutureValue"

