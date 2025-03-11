from __future__ import annotations
from enum import StrEnum


class MultiTenantOrganizationState(StrEnum):
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"

