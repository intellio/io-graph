from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotDeploymentState(StrEnum):
	unknown = "unknown"
	success = "success"
	inProgress = "inProgress"
	failure = "failure"
	successWithTimeout = "successWithTimeout"
	notAttempted = "notAttempted"
	disabled = "disabled"
	successOnRetry = "successOnRetry"

