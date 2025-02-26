from __future__ import annotations
from enum import Enum


class DeviceManagementExchangeAccessState(Enum):
	none = "none"
	unknown = "unknown"
	allowed = "allowed"
	blocked = "blocked"
	quarantined = "quarantined"

