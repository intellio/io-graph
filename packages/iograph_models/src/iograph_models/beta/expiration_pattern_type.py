from __future__ import annotations
from enum import StrEnum


class ExpirationPatternType(StrEnum):
	notSpecified = "notSpecified"
	noExpiration = "noExpiration"
	afterDateTime = "afterDateTime"
	afterDuration = "afterDuration"

