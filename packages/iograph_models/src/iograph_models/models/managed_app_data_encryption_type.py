from __future__ import annotations
from enum import Enum


class ManagedAppDataEncryptionType(Enum):
	useDeviceSettings = "useDeviceSettings"
	afterDeviceRestart = "afterDeviceRestart"
	whenDeviceLockedExceptOpenFiles = "whenDeviceLockedExceptOpenFiles"
	whenDeviceLocked = "whenDeviceLocked"

