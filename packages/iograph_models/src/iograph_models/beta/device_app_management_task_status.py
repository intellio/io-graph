from __future__ import annotations
from enum import StrEnum


class DeviceAppManagementTaskStatus(StrEnum):
	unknown = "unknown"
	pending = "pending"
	active = "active"
	completed = "completed"
	rejected = "rejected"

