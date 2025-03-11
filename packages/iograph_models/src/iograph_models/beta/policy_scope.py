from __future__ import annotations
from enum import StrEnum


class PolicyScope(StrEnum):
	none = "none"
	all = "all"
	selected = "selected"
	unknownFutureValue = "unknownFutureValue"

