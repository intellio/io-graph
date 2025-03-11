from __future__ import annotations
from enum import StrEnum


class MfaFailureReasonCode(StrEnum):
	mfaIncomplete = "mfaIncomplete"
	mfaDenied = "mfaDenied"
	systemFailure = "systemFailure"
	badRequest = "badRequest"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

