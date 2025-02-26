from __future__ import annotations
from enum import Enum


class DeviceManagementSubscriptionState(Enum):
	pending = "pending"
	active = "active"
	warning = "warning"
	disabled = "disabled"
	deleted = "deleted"
	blocked = "blocked"
	lockedOut = "lockedOut"

