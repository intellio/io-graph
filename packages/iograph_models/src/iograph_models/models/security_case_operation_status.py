from __future__ import annotations
from enum import Enum


class SecurityCaseOperationStatus(Enum):
	notStarted = "notStarted"
	submissionFailed = "submissionFailed"
	running = "running"
	succeeded = "succeeded"
	partiallySucceeded = "partiallySucceeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

