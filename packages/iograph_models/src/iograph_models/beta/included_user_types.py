from __future__ import annotations
from enum import StrEnum


class IncludedUserTypes(StrEnum):
	all = "all"
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

