from __future__ import annotations
from enum import StrEnum


class TermStoreTermGroupScope(StrEnum):
	global_ = "global_"
	system = "system"
	siteCollection = "siteCollection"
	unknownFutureValue = "unknownFutureValue"

