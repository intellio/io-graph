from __future__ import annotations
from enum import StrEnum


class AllowedRolePrincipalTypes(StrEnum):
	user = "user"
	servicePrincipal = "servicePrincipal"
	group = "group"
	unknownFutureValue = "unknownFutureValue"

