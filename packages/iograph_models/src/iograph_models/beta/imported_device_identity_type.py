from __future__ import annotations
from enum import StrEnum


class ImportedDeviceIdentityType(StrEnum):
	unknown = "unknown"
	imei = "imei"
	serialNumber = "serialNumber"
	manufacturerModelSerial = "manufacturerModelSerial"

