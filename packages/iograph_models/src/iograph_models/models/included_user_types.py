from __future__ import annotations
from enum import Enum


class IncludedUserTypes(Enum):
	all = "all"
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

