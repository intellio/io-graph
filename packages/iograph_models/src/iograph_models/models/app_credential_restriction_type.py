from __future__ import annotations
from enum import Enum


class AppCredentialRestrictionType(Enum):
	passwordAddition = "passwordAddition"
	passwordLifetime = "passwordLifetime"
	symmetricKeyAddition = "symmetricKeyAddition"
	symmetricKeyLifetime = "symmetricKeyLifetime"
	customPasswordAddition = "customPasswordAddition"
	unknownFutureValue = "unknownFutureValue"

