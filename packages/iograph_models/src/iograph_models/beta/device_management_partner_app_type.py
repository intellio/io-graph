from __future__ import annotations
from enum import StrEnum


class DeviceManagementPartnerAppType(StrEnum):
	unknown = "unknown"
	singleTenantApp = "singleTenantApp"
	multiTenantApp = "multiTenantApp"

