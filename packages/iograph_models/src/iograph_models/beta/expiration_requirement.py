from __future__ import annotations
from enum import StrEnum


class ExpirationRequirement(StrEnum):
	rememberMultifactorAuthenticationOnTrustedDevices = "rememberMultifactorAuthenticationOnTrustedDevices"
	tenantTokenLifetimePolicy = "tenantTokenLifetimePolicy"
	audienceTokenLifetimePolicy = "audienceTokenLifetimePolicy"
	signInFrequencyPeriodicReauthentication = "signInFrequencyPeriodicReauthentication"
	ngcMfa = "ngcMfa"
	signInFrequencyEveryTime = "signInFrequencyEveryTime"
	unknownFutureValue = "unknownFutureValue"

