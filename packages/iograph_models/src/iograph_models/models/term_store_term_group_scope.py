from __future__ import annotations
from enum import Enum


class TermStoreTermGroupScope(Enum):
	global_ = "global_"
	system = "system"
	siteCollection = "siteCollection"
	unknownFutureValue = "unknownFutureValue"

