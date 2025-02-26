from __future__ import annotations
from enum import Enum


class SignInFrequencyAuthenticationType(Enum):
	primaryAndSecondaryAuthentication = "primaryAndSecondaryAuthentication"
	secondaryAuthentication = "secondaryAuthentication"
	unknownFutureValue = "unknownFutureValue"

