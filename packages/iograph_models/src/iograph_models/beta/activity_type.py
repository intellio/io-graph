from __future__ import annotations
from enum import StrEnum


class ActivityType(StrEnum):
	signin = "signin"
	user = "user"
	unknownFutureValue = "unknownFutureValue"
	servicePrincipal = "servicePrincipal"

