from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodPlatform(StrEnum):
	unknown = "unknown"
	windows = "windows"
	macOS = "macOS"
	iOS = "iOS"
	android = "android"
	linux = "linux"
	unknownFutureValue = "unknownFutureValue"

