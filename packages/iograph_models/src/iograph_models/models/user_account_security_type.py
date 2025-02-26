from __future__ import annotations
from enum import Enum


class UserAccountSecurityType(Enum):
	unknown = "unknown"
	standard = "standard"
	power = "power"
	administrator = "administrator"
	unknownFutureValue = "unknownFutureValue"

