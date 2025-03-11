from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerSystemUpdateInstallType(StrEnum):
	deviceDefault = "deviceDefault"
	postpone = "postpone"
	windowed = "windowed"
	automatic = "automatic"

