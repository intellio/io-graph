from __future__ import annotations
from enum import Enum


class ManagedDevicePartnerReportedHealthState(Enum):
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

