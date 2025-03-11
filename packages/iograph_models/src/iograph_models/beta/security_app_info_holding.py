from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoHolding(StrEnum):
	private = "private"
	public = "public"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

