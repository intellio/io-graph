from __future__ import annotations
from enum import StrEnum


class ManagedTenantsManagementCategory(StrEnum):
	custom = "custom"
	devices = "devices"
	identity = "identity"
	data = "data"
	unknownFutureValue = "unknownFutureValue"

