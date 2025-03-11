from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerEnrollmentProfileType(StrEnum):
	notConfigured = "notConfigured"
	dedicatedDevice = "dedicatedDevice"
	fullyManaged = "fullyManaged"

