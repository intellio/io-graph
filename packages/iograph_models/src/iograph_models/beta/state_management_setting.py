from __future__ import annotations
from enum import StrEnum


class StateManagementSetting(StrEnum):
	notConfigured = "notConfigured"
	blocked = "blocked"
	allowed = "allowed"

