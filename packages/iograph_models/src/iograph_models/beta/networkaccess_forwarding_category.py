from __future__ import annotations
from enum import StrEnum


class NetworkaccessForwardingCategory(StrEnum):
	default = "default"
	optimized = "optimized"
	allow = "allow"
	unknownFutureValue = "unknownFutureValue"

