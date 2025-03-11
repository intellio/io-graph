from __future__ import annotations
from enum import StrEnum


class DeviceGuardVirtualizationBasedSecurityState(StrEnum):
	running = "running"
	rebootRequired = "rebootRequired"
	require64BitArchitecture = "require64BitArchitecture"
	notLicensed = "notLicensed"
	notConfigured = "notConfigured"
	doesNotMeetHardwareRequirements = "doesNotMeetHardwareRequirements"
	other = "other"

