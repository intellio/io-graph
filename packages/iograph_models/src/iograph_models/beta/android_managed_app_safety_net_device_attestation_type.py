from __future__ import annotations
from enum import StrEnum


class AndroidManagedAppSafetyNetDeviceAttestationType(StrEnum):
	none = "none"
	basicIntegrity = "basicIntegrity"
	basicIntegrityAndDeviceCertification = "basicIntegrityAndDeviceCertification"

