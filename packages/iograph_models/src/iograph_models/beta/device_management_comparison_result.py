from __future__ import annotations
from enum import StrEnum


class DeviceManagementComparisonResult(StrEnum):
	unknown = "unknown"
	equal = "equal"
	notEqual = "notEqual"
	added = "added"
	removed = "removed"

