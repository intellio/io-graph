from __future__ import annotations
from enum import StrEnum


class ManagedAppFlaggedReason(StrEnum):
	none = "none"
	rootedDevice = "rootedDevice"
	androidBootloaderUnlocked = "androidBootloaderUnlocked"
	androidFactoryRomModified = "androidFactoryRomModified"

