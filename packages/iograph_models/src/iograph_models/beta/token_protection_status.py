from __future__ import annotations
from enum import StrEnum


class TokenProtectionStatus(StrEnum):
	none = "none"
	bound = "bound"
	unbound = "unbound"
	unknownFutureValue = "unknownFutureValue"

