from __future__ import annotations
from enum import StrEnum


class DeviceManagementExchangeAccessState(StrEnum):
	none = "none"
	unknown = "unknown"
	allowed = "allowed"
	blocked = "blocked"
	quarantined = "quarantined"

