from __future__ import annotations
from enum import StrEnum


class DeviceManagementPartnerTenantState(StrEnum):
	unknown = "unknown"
	unavailable = "unavailable"
	enabled = "enabled"
	terminated = "terminated"
	rejected = "rejected"
	unresponsive = "unresponsive"

