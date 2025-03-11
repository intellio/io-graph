from __future__ import annotations
from enum import StrEnum


class CrossTenantAccessPolicyTargetConfigurationAccessType(StrEnum):
	allowed = "allowed"
	blocked = "blocked"
	unknownFutureValue = "unknownFutureValue"

