from __future__ import annotations
from enum import StrEnum


class Fido2RestrictionEnforcementType(StrEnum):
	allow = "allow"
	block = "block"
	unknownFutureValue = "unknownFutureValue"

