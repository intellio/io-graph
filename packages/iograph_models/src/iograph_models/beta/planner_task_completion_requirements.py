from __future__ import annotations
from enum import StrEnum


class PlannerTaskCompletionRequirements(StrEnum):
	none = "none"
	checklistCompletion = "checklistCompletion"
	unknownFutureValue = "unknownFutureValue"
	formCompletion = "formCompletion"
	approvalCompletion = "approvalCompletion"
	completionInHostedApp = "completionInHostedApp"

