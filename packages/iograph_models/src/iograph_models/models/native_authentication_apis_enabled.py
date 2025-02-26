from __future__ import annotations
from enum import Enum


class NativeAuthenticationApisEnabled(Enum):
	none = "none"
	all = "all"
	unknownFutureValue = "unknownFutureValue"

