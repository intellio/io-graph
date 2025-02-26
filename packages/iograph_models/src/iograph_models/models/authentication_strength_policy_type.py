from __future__ import annotations
from enum import Enum


class AuthenticationStrengthPolicyType(Enum):
	builtIn = "builtIn"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

