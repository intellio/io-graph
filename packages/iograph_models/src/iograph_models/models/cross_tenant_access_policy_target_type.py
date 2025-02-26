from __future__ import annotations
from enum import Enum


class CrossTenantAccessPolicyTargetType(Enum):
	user = "user"
	group = "group"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

