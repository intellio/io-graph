from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceLifecycleWorkflowProcessingStatus(StrEnum):
	queued = "queued"
	inProgress = "inProgress"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	canceled = "canceled"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

