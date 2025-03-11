from __future__ import annotations
from enum import StrEnum


class ManagedDeviceArchitecture(StrEnum):
	unknown = "unknown"
	x86 = "x86"
	x64 = "x64"
	arm = "arm"
	arM64 = "arM64"

