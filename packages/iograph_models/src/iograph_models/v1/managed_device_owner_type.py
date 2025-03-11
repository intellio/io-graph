from __future__ import annotations
from enum import StrEnum


class ManagedDeviceOwnerType(StrEnum):
	unknown = "unknown"
	company = "company"
	personal = "personal"
	unknownFutureValue = "unknownFutureValue"

