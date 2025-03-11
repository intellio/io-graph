from __future__ import annotations
from enum import StrEnum


class ManagedTenantsDelegatedPrivilegeStatus(StrEnum):
	none = "none"
	delegatedAdminPrivileges = "delegatedAdminPrivileges"
	unknownFutureValue = "unknownFutureValue"
	granularDelegatedAdminPrivileges = "granularDelegatedAdminPrivileges"
	delegatedAndGranularDelegetedAdminPrivileges = "delegatedAndGranularDelegetedAdminPrivileges"

