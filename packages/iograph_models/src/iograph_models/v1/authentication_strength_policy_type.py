from __future__ import annotations
from enum import StrEnum


class AuthenticationStrengthPolicyType(StrEnum):
	builtIn = "builtIn"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

