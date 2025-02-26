from __future__ import annotations
from enum import Enum


class TargettedUserType(Enum):
	unknown = "unknown"
	clicked = "clicked"
	compromised = "compromised"
	allUsers = "allUsers"
	unknownFutureValue = "unknownFutureValue"

