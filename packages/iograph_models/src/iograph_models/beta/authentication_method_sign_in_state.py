from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodSignInState(StrEnum):
	notSupported = "notSupported"
	notAllowedByPolicy = "notAllowedByPolicy"
	notEnabled = "notEnabled"
	phoneNumberNotUnique = "phoneNumberNotUnique"
	ready = "ready"
	notConfigured = "notConfigured"
	unknownFutureValue = "unknownFutureValue"

