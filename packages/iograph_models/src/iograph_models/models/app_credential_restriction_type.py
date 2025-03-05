from __future__ import annotations
from enum import StrEnum


class AppCredentialRestrictionType(StrEnum):
	passwordAddition = "passwordAddition"
	passwordLifetime = "passwordLifetime"
	symmetricKeyAddition = "symmetricKeyAddition"
	symmetricKeyLifetime = "symmetricKeyLifetime"
	customPasswordAddition = "customPasswordAddition"
	unknownFutureValue = "unknownFutureValue"

