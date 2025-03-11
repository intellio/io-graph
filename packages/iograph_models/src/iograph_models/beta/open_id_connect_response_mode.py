from __future__ import annotations
from enum import StrEnum


class OpenIdConnectResponseMode(StrEnum):
	form_post = "form_post"
	query = "query"
	unknownFutureValue = "unknownFutureValue"

