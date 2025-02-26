from __future__ import annotations
from enum import Enum


class MultiTenantOrganizationMemberProcessingStatus(Enum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

