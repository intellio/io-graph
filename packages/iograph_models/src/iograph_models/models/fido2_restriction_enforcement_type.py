from __future__ import annotations
from enum import Enum


class Fido2RestrictionEnforcementType(Enum):
	allow = "allow"
	block = "block"
	unknownFutureValue = "unknownFutureValue"

