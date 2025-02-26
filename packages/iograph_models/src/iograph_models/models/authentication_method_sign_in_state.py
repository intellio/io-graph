from __future__ import annotations
from enum import Enum


class AuthenticationMethodSignInState(Enum):
	notSupported = "notSupported"
	notAllowedByPolicy = "notAllowedByPolicy"
	notEnabled = "notEnabled"
	phoneNumberNotUnique = "phoneNumberNotUnique"
	ready = "ready"
	notConfigured = "notConfigured"
	unknownFutureValue = "unknownFutureValue"

