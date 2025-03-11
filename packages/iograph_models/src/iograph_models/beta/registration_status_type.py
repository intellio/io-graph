from __future__ import annotations
from enum import StrEnum


class RegistrationStatusType(StrEnum):
	registered = "registered"
	enabled = "enabled"
	capable = "capable"
	mfaRegistered = "mfaRegistered"
	unknownFutureValue = "unknownFutureValue"

