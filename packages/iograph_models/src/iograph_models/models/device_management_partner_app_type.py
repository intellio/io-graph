from __future__ import annotations
from enum import Enum


class DeviceManagementPartnerAppType(Enum):
	unknown = "unknown"
	singleTenantApp = "singleTenantApp"
	multiTenantApp = "multiTenantApp"

