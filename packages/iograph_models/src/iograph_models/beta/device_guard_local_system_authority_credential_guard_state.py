from __future__ import annotations
from enum import StrEnum


class DeviceGuardLocalSystemAuthorityCredentialGuardState(StrEnum):
	running = "running"
	rebootRequired = "rebootRequired"
	notLicensed = "notLicensed"
	notConfigured = "notConfigured"
	virtualizationBasedSecurityNotRunning = "virtualizationBasedSecurityNotRunning"

