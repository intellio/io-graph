from __future__ import annotations
from enum import StrEnum


class SignInFrequencyAuthenticationType(StrEnum):
	primaryAndSecondaryAuthentication = "primaryAndSecondaryAuthentication"
	secondaryAuthentication = "secondaryAuthentication"
	unknownFutureValue = "unknownFutureValue"

