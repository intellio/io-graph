from __future__ import annotations
from enum import StrEnum


class AndroidProfileApplicability(StrEnum):
	default = "default"
	androidWorkProfile = "androidWorkProfile"
	androidDeviceOwner = "androidDeviceOwner"

