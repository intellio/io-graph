from __future__ import annotations
from enum import Enum


class IdentityGovernanceLifecycleWorkflowProcessingStatus(Enum):
	queued = "queued"
	inProgress = "inProgress"
	completed = "completed"
	completedWithErrors = "completedWithErrors"
	canceled = "canceled"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

