from __future__ import annotations
from enum import StrEnum


class SignInIdentifierType(StrEnum):
	userPrincipalName = "userPrincipalName"
	phoneNumber = "phoneNumber"
	proxyAddress = "proxyAddress"
	qrCode = "qrCode"
	onPremisesUserPrincipalName = "onPremisesUserPrincipalName"
	unknownFutureValue = "unknownFutureValue"

