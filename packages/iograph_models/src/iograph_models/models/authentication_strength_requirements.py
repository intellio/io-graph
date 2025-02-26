from __future__ import annotations
from enum import Enum


class AuthenticationStrengthRequirements(Enum):
	none = "none"
	mfa = "mfa"
	unknownFutureValue = "unknownFutureValue"

