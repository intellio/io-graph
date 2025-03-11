from __future__ import annotations
from enum import StrEnum


class ManagedAppDataEncryptionType(StrEnum):
	useDeviceSettings = "useDeviceSettings"
	afterDeviceRestart = "afterDeviceRestart"
	whenDeviceLockedExceptOpenFiles = "whenDeviceLockedExceptOpenFiles"
	whenDeviceLocked = "whenDeviceLocked"

