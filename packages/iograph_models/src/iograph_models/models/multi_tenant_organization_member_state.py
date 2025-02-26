from __future__ import annotations
from enum import Enum


class MultiTenantOrganizationMemberState(Enum):
	pending = "pending"
	active = "active"
	removed = "removed"
	unknownFutureValue = "unknownFutureValue"

