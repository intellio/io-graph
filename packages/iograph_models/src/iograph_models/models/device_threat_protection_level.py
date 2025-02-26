from __future__ import annotations
from enum import Enum


class DeviceThreatProtectionLevel(Enum):
	unavailable = "unavailable"
	secured = "secured"
	low = "low"
	medium = "medium"
	high = "high"
	notSet = "notSet"

