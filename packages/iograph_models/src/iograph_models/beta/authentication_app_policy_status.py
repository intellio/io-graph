from __future__ import annotations
from enum import StrEnum


class AuthenticationAppPolicyStatus(StrEnum):
	unknown = "unknown"
	appLockOutOfDate = "appLockOutOfDate"
	appLockEnabled = "appLockEnabled"
	appLockDisabled = "appLockDisabled"
	appContextOutOfDate = "appContextOutOfDate"
	appContextShown = "appContextShown"
	appContextNotShown = "appContextNotShown"
	locationContextOutOfDate = "locationContextOutOfDate"
	locationContextShown = "locationContextShown"
	locationContextNotShown = "locationContextNotShown"
	numberMatchOutOfDate = "numberMatchOutOfDate"
	numberMatchCorrectNumberEntered = "numberMatchCorrectNumberEntered"
	numberMatchIncorrectNumberEntered = "numberMatchIncorrectNumberEntered"
	numberMatchDeny = "numberMatchDeny"
	tamperResistantHardwareOutOfDate = "tamperResistantHardwareOutOfDate"
	tamperResistantHardwareUsed = "tamperResistantHardwareUsed"
	tamperResistantHardwareNotUsed = "tamperResistantHardwareNotUsed"
	unknownFutureValue = "unknownFutureValue"

