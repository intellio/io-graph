from __future__ import annotations
from enum import Enum


class SignInUserType(Enum):
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

