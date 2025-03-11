from __future__ import annotations
from enum import StrEnum


class ManagedTenantsManagementProvider(StrEnum):
	microsoft = "microsoft"
	community = "community"
	indirectProvider = "indirectProvider"
	self = "self"
	unknownFutureValue = "unknownFutureValue"

