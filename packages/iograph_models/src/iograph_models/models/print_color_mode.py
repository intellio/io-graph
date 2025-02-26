from __future__ import annotations
from enum import Enum


class PrintColorMode(Enum):
	blackAndWhite = "blackAndWhite"
	grayscale = "grayscale"
	color = "color"
	auto = "auto"
	unknownFutureValue = "unknownFutureValue"

