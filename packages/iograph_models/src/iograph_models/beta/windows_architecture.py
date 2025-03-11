from __future__ import annotations
from enum import StrEnum


class WindowsArchitecture(StrEnum):
	none = "none"
	x86 = "x86"
	x64 = "x64"
	arm = "arm"
	neutral = "neutral"
	arm64 = "arm64"

