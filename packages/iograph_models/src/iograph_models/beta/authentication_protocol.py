from __future__ import annotations
from enum import StrEnum


class AuthenticationProtocol(StrEnum):
	wsFed = "wsFed"
	saml = "saml"
	unknownFutureValue = "unknownFutureValue"

