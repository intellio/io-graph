from __future__ import annotations
from enum import StrEnum


class SignInUserType(StrEnum):
	member = "member"
	guest = "guest"
	unknownFutureValue = "unknownFutureValue"

