from __future__ import annotations
from enum import StrEnum


class RoleAssignmentScopeType(StrEnum):
	resourceScope = "resourceScope"
	allDevices = "allDevices"
	allLicensedUsers = "allLicensedUsers"
	allDevicesAndLicensedUsers = "allDevicesAndLicensedUsers"

