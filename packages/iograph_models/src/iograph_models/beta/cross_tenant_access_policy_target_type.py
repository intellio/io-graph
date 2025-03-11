from __future__ import annotations
from enum import StrEnum


class CrossTenantAccessPolicyTargetType(StrEnum):
	user = "user"
	group = "group"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

