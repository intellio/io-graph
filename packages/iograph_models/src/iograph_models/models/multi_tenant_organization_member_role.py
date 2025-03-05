from __future__ import annotations
from enum import StrEnum


class MultiTenantOrganizationMemberRole(StrEnum):
	owner = "owner"
	member = "member"
	unknownFutureValue = "unknownFutureValue"

