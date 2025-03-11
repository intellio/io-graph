from __future__ import annotations
from enum import StrEnum


class UserAccountSecurityType(StrEnum):
	unknown = "unknown"
	standard = "standard"
	power = "power"
	administrator = "administrator"
	unknownFutureValue = "unknownFutureValue"

