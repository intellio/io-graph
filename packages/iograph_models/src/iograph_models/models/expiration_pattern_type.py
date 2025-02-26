from __future__ import annotations
from enum import Enum


class ExpirationPatternType(Enum):
	notSpecified = "notSpecified"
	noExpiration = "noExpiration"
	afterDateTime = "afterDateTime"
	afterDuration = "afterDuration"

