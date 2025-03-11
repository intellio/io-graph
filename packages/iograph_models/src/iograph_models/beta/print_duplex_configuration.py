from __future__ import annotations
from enum import StrEnum


class PrintDuplexConfiguration(StrEnum):
	twoSidedLongEdge = "twoSidedLongEdge"
	twoSidedShortEdge = "twoSidedShortEdge"
	oneSided = "oneSided"

