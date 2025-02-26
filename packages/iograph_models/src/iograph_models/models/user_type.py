from __future__ import annotations
from enum import Enum


class UserType(Enum):
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

