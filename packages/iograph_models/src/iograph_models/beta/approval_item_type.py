from __future__ import annotations
from enum import StrEnum


class ApprovalItemType(StrEnum):
	basic = "basic"
	basicAwaitAll = "basicAwaitAll"
	custom = "custom"
	customAwaitAll = "customAwaitAll"
	unknownFutureValue = "unknownFutureValue"

