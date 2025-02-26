from __future__ import annotations
from enum import Enum


class ActivityType(Enum):
	signin = "signin"
	user = "user"
	unknownFutureValue = "unknownFutureValue"
	servicePrincipal = "servicePrincipal"

