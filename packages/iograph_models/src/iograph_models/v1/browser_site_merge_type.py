from __future__ import annotations
from enum import StrEnum


class BrowserSiteMergeType(StrEnum):
	noMerge = "noMerge"
	default = "default"
	unknownFutureValue = "unknownFutureValue"

