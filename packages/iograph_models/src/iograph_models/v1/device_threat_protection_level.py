from __future__ import annotations
from enum import StrEnum


class DeviceThreatProtectionLevel(StrEnum):
	unavailable = "unavailable"
	secured = "secured"
	low = "low"
	medium = "medium"
	high = "high"
	notSet = "notSet"

