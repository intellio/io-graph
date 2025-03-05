from __future__ import annotations
from enum import StrEnum


class SecurityDefenderAvStatus(StrEnum):
	notReporting = "notReporting"
	disabled = "disabled"
	notUpdated = "notUpdated"
	updated = "updated"
	unknown = "unknown"
	notSupported = "notSupported"
	unknownFutureValue = "unknownFutureValue"

