from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerEnrollmentMode(StrEnum):
	corporateOwnedDedicatedDevice = "corporateOwnedDedicatedDevice"
	corporateOwnedFullyManaged = "corporateOwnedFullyManaged"
	corporateOwnedWorkProfile = "corporateOwnedWorkProfile"
	corporateOwnedAOSPUserlessDevice = "corporateOwnedAOSPUserlessDevice"
	corporateOwnedAOSPUserAssociatedDevice = "corporateOwnedAOSPUserAssociatedDevice"

