from __future__ import annotations
from enum import Enum


class MultiTenantOrganizationMemberRole(Enum):
	owner = "owner"
	member = "member"
	unknownFutureValue = "unknownFutureValue"

