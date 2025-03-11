from __future__ import annotations
from enum import StrEnum


class DeviceGuardLocalSystemAuthorityCredentialGuardType(StrEnum):
	notConfigured = "notConfigured"
	enableWithUEFILock = "enableWithUEFILock"
	enableWithoutUEFILock = "enableWithoutUEFILock"
	disable = "disable"

