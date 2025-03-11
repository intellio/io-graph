from __future__ import annotations
from enum import StrEnum


class ManagedAppLogUploadConsent(StrEnum):
	unknown = "unknown"
	declined = "declined"
	accepted = "accepted"
	unknownFutureValue = "unknownFutureValue"

