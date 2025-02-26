from __future__ import annotations
from enum import Enum


class MultiTenantOrganizationState(Enum):
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"

