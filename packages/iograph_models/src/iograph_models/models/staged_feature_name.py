from __future__ import annotations
from enum import StrEnum


class StagedFeatureName(StrEnum):
	passthroughAuthentication = "passthroughAuthentication"
	seamlessSso = "seamlessSso"
	passwordHashSync = "passwordHashSync"
	emailAsAlternateId = "emailAsAlternateId"
	unknownFutureValue = "unknownFutureValue"
	certificateBasedAuthentication = "certificateBasedAuthentication"
	multiFactorAuthentication = "multiFactorAuthentication"

