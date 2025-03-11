from __future__ import annotations
from enum import StrEnum


class IncludedUserRoles(StrEnum):
	all = "all"
	privilegedAdmin = "privilegedAdmin"
	admin = "admin"
	user = "user"
	unknownFutureValue = "unknownFutureValue"

