from __future__ import annotations
from enum import StrEnum


class SecurityIndicatorSource(StrEnum):
	microsoft = "microsoft"
	osint = "osint"
	public = "public"
	unknownFutureValue = "unknownFutureValue"

