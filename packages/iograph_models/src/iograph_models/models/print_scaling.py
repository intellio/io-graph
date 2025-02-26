from __future__ import annotations
from enum import Enum


class PrintScaling(Enum):
	auto = "auto"
	shrinkToFit = "shrinkToFit"
	fill = "fill"
	fit = "fit"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

