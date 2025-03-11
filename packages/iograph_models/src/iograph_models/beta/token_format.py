from __future__ import annotations
from enum import StrEnum


class TokenFormat(StrEnum):
	saml = "saml"
	jwt = "jwt"
	unknownFutureValue = "unknownFutureValue"

