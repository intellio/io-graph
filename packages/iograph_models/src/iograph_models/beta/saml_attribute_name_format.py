from __future__ import annotations
from enum import StrEnum


class SamlAttributeNameFormat(StrEnum):
	unspecified = "unspecified"
	uri = "uri"
	basic = "basic"
	unknownFutureValue = "unknownFutureValue"

