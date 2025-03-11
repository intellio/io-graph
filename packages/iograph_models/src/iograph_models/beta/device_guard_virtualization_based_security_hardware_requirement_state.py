from __future__ import annotations
from enum import StrEnum


class DeviceGuardVirtualizationBasedSecurityHardwareRequirementState(StrEnum):
	meetHardwareRequirements = "meetHardwareRequirements"
	secureBootRequired = "secureBootRequired"
	dmaProtectionRequired = "dmaProtectionRequired"
	hyperVNotSupportedForGuestVM = "hyperVNotSupportedForGuestVM"
	hyperVNotAvailable = "hyperVNotAvailable"

