from __future__ import annotations
from enum import Enum


class CrossTenantAccessPolicyTargetConfigurationAccessType(Enum):
	allowed = "allowed"
	blocked = "blocked"
	unknownFutureValue = "unknownFutureValue"

