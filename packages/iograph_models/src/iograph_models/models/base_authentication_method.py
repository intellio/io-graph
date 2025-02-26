from __future__ import annotations
from enum import Enum


class BaseAuthenticationMethod(Enum):
	password = "password"
	voice = "voice"
	hardwareOath = "hardwareOath"
	softwareOath = "softwareOath"
	sms = "sms"
	fido2 = "fido2"
	windowsHelloForBusiness = "windowsHelloForBusiness"
	microsoftAuthenticator = "microsoftAuthenticator"
	temporaryAccessPass = "temporaryAccessPass"
	email = "email"
	x509Certificate = "x509Certificate"
	federation = "federation"
	unknownFutureValue = "unknownFutureValue"

