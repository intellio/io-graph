from __future__ import annotations
from enum import StrEnum


class TargettedUserType(StrEnum):
	unknown = "unknown"
	clicked = "clicked"
	compromised = "compromised"
	allUsers = "allUsers"
	unknownFutureValue = "unknownFutureValue"

