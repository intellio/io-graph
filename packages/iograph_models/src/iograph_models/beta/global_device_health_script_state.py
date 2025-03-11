from __future__ import annotations
from enum import StrEnum


class GlobalDeviceHealthScriptState(StrEnum):
	notConfigured = "notConfigured"
	pending = "pending"
	enabled = "enabled"

