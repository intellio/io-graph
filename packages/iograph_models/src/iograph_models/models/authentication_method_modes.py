from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodModes(StrEnum):
	password = "password"
	voice = "voice"
	hardwareOath = "hardwareOath"
	softwareOath = "softwareOath"
	sms = "sms"
	fido2 = "fido2"
	windowsHelloForBusiness = "windowsHelloForBusiness"
	microsoftAuthenticatorPush = "microsoftAuthenticatorPush"
	deviceBasedPush = "deviceBasedPush"
	temporaryAccessPassOneTime = "temporaryAccessPassOneTime"
	temporaryAccessPassMultiUse = "temporaryAccessPassMultiUse"
	email = "email"
	x509CertificateSingleFactor = "x509CertificateSingleFactor"
	x509CertificateMultiFactor = "x509CertificateMultiFactor"
	federatedSingleFactor = "federatedSingleFactor"
	federatedMultiFactor = "federatedMultiFactor"
	unknownFutureValue = "unknownFutureValue"

