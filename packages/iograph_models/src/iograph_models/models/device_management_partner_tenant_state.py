from __future__ import annotations
from enum import Enum


class DeviceManagementPartnerTenantState(Enum):
	unknown = "unknown"
	unavailable = "unavailable"
	enabled = "enabled"
	terminated = "terminated"
	rejected = "rejected"
	unresponsive = "unresponsive"

