from __future__ import annotations
from enum import StrEnum


class DeviceManagementSubscriptionState(StrEnum):
	pending = "pending"
	active = "active"
	warning = "warning"
	disabled = "disabled"
	deleted = "deleted"
	blocked = "blocked"
	lockedOut = "lockedOut"

