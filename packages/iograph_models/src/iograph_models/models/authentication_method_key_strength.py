from __future__ import annotations
from enum import Enum


class AuthenticationMethodKeyStrength(Enum):
	normal = "normal"
	weak = "weak"
	unknown = "unknown"

