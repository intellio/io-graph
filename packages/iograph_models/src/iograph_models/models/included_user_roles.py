from __future__ import annotations
from enum import Enum


class IncludedUserRoles(Enum):
	all = "all"
	privilegedAdmin = "privilegedAdmin"
	admin = "admin"
	user = "user"
	unknownFutureValue = "unknownFutureValue"

