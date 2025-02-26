from __future__ import annotations
from enum import Enum


class AuthenticationProtocol(Enum):
	wsFed = "wsFed"
	saml = "saml"
	unknownFutureValue = "unknownFutureValue"

