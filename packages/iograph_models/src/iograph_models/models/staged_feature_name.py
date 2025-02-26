from __future__ import annotations
from enum import Enum


class StagedFeatureName(Enum):
	passthroughAuthentication = "passthroughAuthentication"
	seamlessSso = "seamlessSso"
	passwordHashSync = "passwordHashSync"
	emailAsAlternateId = "emailAsAlternateId"
	unknownFutureValue = "unknownFutureValue"
	certificateBasedAuthentication = "certificateBasedAuthentication"
	multiFactorAuthentication = "multiFactorAuthentication"

