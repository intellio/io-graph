from __future__ import annotations
from enum import StrEnum


class NativeAuthenticationApisEnabled(StrEnum):
	none = "none"
	all = "all"
	unknownFutureValue = "unknownFutureValue"

