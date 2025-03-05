from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodTargetType(StrEnum):
	user = "user"
	group = "group"
	unknownFutureValue = "unknownFutureValue"

