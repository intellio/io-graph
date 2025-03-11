from __future__ import annotations
from enum import StrEnum


class SecurityRecipientType(StrEnum):
	user = "user"
	roleGroup = "roleGroup"
	unknownFutureValue = "unknownFutureValue"

