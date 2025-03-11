from __future__ import annotations
from enum import StrEnum


class OidcResponseType(StrEnum):
	code = "code"
	id_token = "id_token"
	token = "token"
	unknownFutureValue = "unknownFutureValue"

