from __future__ import annotations
from enum import StrEnum


class MobileAppSupersedenceType(StrEnum):
	update = "update"
	replace = "replace"
	unknownFutureValue = "unknownFutureValue"

