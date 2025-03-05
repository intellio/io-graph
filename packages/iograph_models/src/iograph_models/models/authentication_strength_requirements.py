from __future__ import annotations
from enum import StrEnum


class AuthenticationStrengthRequirements(StrEnum):
	none = "none"
	mfa = "mfa"
	unknownFutureValue = "unknownFutureValue"

