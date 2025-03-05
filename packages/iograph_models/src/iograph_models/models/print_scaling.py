from __future__ import annotations
from enum import StrEnum


class PrintScaling(StrEnum):
	auto = "auto"
	shrinkToFit = "shrinkToFit"
	fill = "fill"
	fit = "fit"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

