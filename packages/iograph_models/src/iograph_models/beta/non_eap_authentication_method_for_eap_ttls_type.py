from __future__ import annotations
from enum import StrEnum


class NonEapAuthenticationMethodForEapTtlsType(StrEnum):
	unencryptedPassword = "unencryptedPassword"
	challengeHandshakeAuthenticationProtocol = "challengeHandshakeAuthenticationProtocol"
	microsoftChap = "microsoftChap"
	microsoftChapVersionTwo = "microsoftChapVersionTwo"

