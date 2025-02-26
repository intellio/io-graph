from __future__ import annotations
from enum import Enum


class ProtectionPolicyStatus(Enum):
	inactive = "inactive"
	activeWithErrors = "activeWithErrors"
	updating = "updating"
	active = "active"
	unknownFutureValue = "unknownFutureValue"

