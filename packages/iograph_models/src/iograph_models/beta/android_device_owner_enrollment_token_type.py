from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerEnrollmentTokenType(StrEnum):
	default = "default"
	corporateOwnedDedicatedDeviceWithAzureADSharedMode = "corporateOwnedDedicatedDeviceWithAzureADSharedMode"
	deviceStaging = "deviceStaging"

