from __future__ import annotations
from enum import StrEnum


class AndroidManagedStoreAutoUpdateMode(StrEnum):
	default = "default"
	postponed = "postponed"
	priority = "priority"
	unknownFutureValue = "unknownFutureValue"

