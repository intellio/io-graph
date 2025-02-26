from __future__ import annotations
from enum import Enum


class AuthenticationMethodFeature(Enum):
	ssprRegistered = "ssprRegistered"
	ssprEnabled = "ssprEnabled"
	ssprCapable = "ssprCapable"
	passwordlessCapable = "passwordlessCapable"
	mfaCapable = "mfaCapable"
	unknownFutureValue = "unknownFutureValue"

