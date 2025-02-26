from __future__ import annotations
from enum import Enum


class SecurityResourceType(Enum):
	unknown = "unknown"
	attacked = "attacked"
	related = "related"
	unknownFutureValue = "unknownFutureValue"

