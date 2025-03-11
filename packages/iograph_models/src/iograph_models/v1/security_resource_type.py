from __future__ import annotations
from enum import StrEnum


class SecurityResourceType(StrEnum):
	unknown = "unknown"
	attacked = "attacked"
	related = "related"
	unknownFutureValue = "unknownFutureValue"

