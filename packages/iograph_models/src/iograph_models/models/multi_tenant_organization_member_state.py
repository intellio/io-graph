from __future__ import annotations
from enum import StrEnum


class MultiTenantOrganizationMemberState(StrEnum):
	pending = "pending"
	active = "active"
	removed = "removed"
	unknownFutureValue = "unknownFutureValue"

