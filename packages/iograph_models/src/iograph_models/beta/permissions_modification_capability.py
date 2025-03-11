from __future__ import annotations
from enum import StrEnum


class PermissionsModificationCapability(StrEnum):
	enabled = "enabled"
	notConfigured = "notConfigured"
	noRecentDataCollected = "noRecentDataCollected"
	unknownFutureValue = "unknownFutureValue"

