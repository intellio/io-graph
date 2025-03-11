from __future__ import annotations
from enum import StrEnum


class ManagedAppDeviceThreatLevel(StrEnum):
	notConfigured = "notConfigured"
	secured = "secured"
	low = "low"
	medium = "medium"
	high = "high"

