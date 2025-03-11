from __future__ import annotations
from enum import StrEnum


class ChangeItemState(StrEnum):
	available = "available"
	comingSoon = "comingSoon"
	unknownFutureValue = "unknownFutureValue"

