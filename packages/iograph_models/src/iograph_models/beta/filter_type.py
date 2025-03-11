from __future__ import annotations
from enum import StrEnum


class FilterType(StrEnum):
	prefix = "prefix"
	suffix = "suffix"
	contains = "contains"
	unknownFutureValue = "unknownFutureValue"

