from __future__ import annotations
from enum import Enum


class AuthenticationMethodTargetType(Enum):
	user = "user"
	group = "group"
	unknownFutureValue = "unknownFutureValue"

