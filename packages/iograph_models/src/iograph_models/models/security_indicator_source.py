from __future__ import annotations
from enum import Enum


class SecurityIndicatorSource(Enum):
	microsoft = "microsoft"
	osint = "osint"
	public = "public"
	unknownFutureValue = "unknownFutureValue"

