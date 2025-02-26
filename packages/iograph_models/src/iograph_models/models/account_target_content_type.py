from __future__ import annotations
from enum import Enum


class AccountTargetContentType(Enum):
	unknown = "unknown"
	includeAll = "includeAll"
	addressBook = "addressBook"
	unknownFutureValue = "unknownFutureValue"

