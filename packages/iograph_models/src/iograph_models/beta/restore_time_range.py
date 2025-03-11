from __future__ import annotations
from enum import StrEnum


class RestoreTimeRange(StrEnum):
	before = "before"
	after = "after"
	beforeOrAfter = "beforeOrAfter"
	unknownFutureValue = "unknownFutureValue"

