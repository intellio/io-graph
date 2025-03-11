from __future__ import annotations
from enum import StrEnum


class AppManagementLevel(StrEnum):
	unspecified = "unspecified"
	unmanaged = "unmanaged"
	mdm = "mdm"
	androidEnterprise = "androidEnterprise"
	androidEnterpriseDedicatedDevicesWithAzureAdSharedMode = "androidEnterpriseDedicatedDevicesWithAzureAdSharedMode"
	androidOpenSourceProjectUserAssociated = "androidOpenSourceProjectUserAssociated"
	androidOpenSourceProjectUserless = "androidOpenSourceProjectUserless"
	unknownFutureValue = "unknownFutureValue"

