from __future__ import annotations
from enum import StrEnum


class AuthenticationFailureReasonCode(StrEnum):
	incomplete = "incomplete"
	denied = "denied"
	systemFailure = "systemFailure"
	badRequest = "badRequest"
	other = "other"
	unknownFutureValue = "unknownFutureValue"
	userError = "userError"
	configError = "configError"

