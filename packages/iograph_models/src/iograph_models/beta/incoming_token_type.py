from __future__ import annotations
from enum import StrEnum


class IncomingTokenType(StrEnum):
	none = "none"
	primaryRefreshToken = "primaryRefreshToken"
	saml11 = "saml11"
	saml20 = "saml20"
	unknownFutureValue = "unknownFutureValue"
	remoteDesktopToken = "remoteDesktopToken"
	refreshToken = "refreshToken"

