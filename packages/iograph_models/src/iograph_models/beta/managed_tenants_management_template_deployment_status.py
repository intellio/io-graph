from __future__ import annotations
from enum import StrEnum


class ManagedTenantsManagementTemplateDeploymentStatus(StrEnum):
	unknown = "unknown"
	inProgress = "inProgress"
	completed = "completed"
	failed = "failed"
	ineligible = "ineligible"
	unknownFutureValue = "unknownFutureValue"

