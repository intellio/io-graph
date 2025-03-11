from __future__ import annotations
from enum import StrEnum


class ManagedTenantsTenantOnboardingEligibilityReason(StrEnum):
	none = "none"
	contractType = "contractType"
	delegatedAdminPrivileges = "delegatedAdminPrivileges"
	usersCount = "usersCount"
	license = "license"
	unknownFutureValue = "unknownFutureValue"

