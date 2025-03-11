from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodFeature(StrEnum):
	ssprRegistered = "ssprRegistered"
	ssprEnabled = "ssprEnabled"
	ssprCapable = "ssprCapable"
	passwordlessCapable = "passwordlessCapable"
	mfaCapable = "mfaCapable"
	unknownFutureValue = "unknownFutureValue"

