from __future__ import annotations
from enum import StrEnum


class ProtocolType(StrEnum):
	none = "none"
	oAuth2 = "oAuth2"
	ropc = "ropc"
	wsFederation = "wsFederation"
	saml20 = "saml20"
	deviceCode = "deviceCode"
	unknownFutureValue = "unknownFutureValue"
	authenticationTransfer = "authenticationTransfer"
	nativeAuth = "nativeAuth"

