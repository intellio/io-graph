from __future__ import annotations
from enum import StrEnum


class DiscoverySource(StrEnum):
	unknown = "unknown"
	adminImport = "adminImport"
	deviceEnrollmentProgram = "deviceEnrollmentProgram"

