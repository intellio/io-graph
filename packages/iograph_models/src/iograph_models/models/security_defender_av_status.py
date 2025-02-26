from __future__ import annotations
from enum import Enum


class SecurityDefenderAvStatus(Enum):
	notReporting = "notReporting"
	disabled = "disabled"
	notUpdated = "notUpdated"
	updated = "updated"
	unknown = "unknown"
	notSupported = "notSupported"
	unknownFutureValue = "unknownFutureValue"

