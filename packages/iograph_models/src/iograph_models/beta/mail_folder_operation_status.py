from __future__ import annotations
from enum import StrEnum


class MailFolderOperationStatus(StrEnum):
	notStarted = "notStarted"
	running = "running"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

