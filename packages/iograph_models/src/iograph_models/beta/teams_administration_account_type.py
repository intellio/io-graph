from __future__ import annotations
from enum import StrEnum


class TeamsAdministrationAccountType(StrEnum):
	user = "user"
	resourceAccount = "resourceAccount"
	guest = "guest"
	sfbOnPremUser = "sfbOnPremUser"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

