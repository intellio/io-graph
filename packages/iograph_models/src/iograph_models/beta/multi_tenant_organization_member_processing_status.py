from __future__ import annotations
from enum import StrEnum


class MultiTenantOrganizationMemberProcessingStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

