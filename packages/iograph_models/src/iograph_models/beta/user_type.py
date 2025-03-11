from __future__ import annotations
from enum import StrEnum


class UserType(StrEnum):
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

