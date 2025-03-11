from __future__ import annotations
from enum import StrEnum


class ManagedDevicePartnerReportedHealthState(StrEnum):
	unknown = "unknown"
	activated = "activated"
	deactivated = "deactivated"
	secured = "secured"
	lowSeverity = "lowSeverity"
	mediumSeverity = "mediumSeverity"
	highSeverity = "highSeverity"
	unresponsive = "unresponsive"
	compromised = "compromised"
	misconfigured = "misconfigured"

