from __future__ import annotations
from enum import StrEnum


class ProtectionPolicyStatus(StrEnum):
	inactive = "inactive"
	activeWithErrors = "activeWithErrors"
	updating = "updating"
	active = "active"
	unknownFutureValue = "unknownFutureValue"

