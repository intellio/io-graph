from __future__ import annotations
from enum import StrEnum


class AccountTargetContentType(StrEnum):
	unknown = "unknown"
	includeAll = "includeAll"
	addressBook = "addressBook"
	unknownFutureValue = "unknownFutureValue"

