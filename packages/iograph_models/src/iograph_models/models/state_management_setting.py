from __future__ import annotations
from enum import Enum


class StateManagementSetting(Enum):
	notConfigured = "notConfigured"
	blocked = "blocked"
	allowed = "allowed"

